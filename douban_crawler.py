import requests
from bs4 import BeautifulSoup
import csv
import time
import re

# 准备CSV文件
csv_file_path = 'douban_top250_movies.csv'
try:

    with open(csv_file_path, 'w', newline='', encoding='utf-8-sig') as f:
        # 定义表头
        fieldnames = [
            '排名', '标题', '链接', '导演', '主演',
            '年份', '国家', '类型', '评分', '评价人数', '一句话评价'
        ]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        # 写入表头
        writer.writeheader()

        # 定义请求头，模拟浏览器访问
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8'
        }

        print("开始爬取豆瓣电影Top250完整数据...")

        rank = 1  # 初始化排名
        # 豆瓣Top250共10页，每页25条，步长为25
        for start_num in range(0, 250, 25):
            url = f'https://movie.douban.com/top250?start={start_num}'
            print(f"正在爬取页面: {url}")

            try:
                response = requests.get(url, headers=headers)
                # 如果请求失败，则抛出异常
                response.raise_for_status()
                response.encoding = 'utf-8'

                soup = BeautifulSoup(response.text, 'html.parser')
                # 找到所有包含电影信息的div
                movie_items = soup.find_all("div", class_="info")

                for item in movie_items:
                    # 电影排名
                    print(f'--- rank{rank} ---')

                    # 1. 获取标题和链接
                    hd_div = item.find('div', class_='hd')
                    title = hd_div.find('span', class_='title').get_text(strip=True)
                    link = hd_div.a['href']

                    print('title: ',title,', url_link: ',link)

                    # 2. 获取电影基本信息（导演、主演、年份、国家、类型）
                    bd_p = item.find('div', class_='bd').find('p')
                    info_text = bd_p.get_text(strip=True, separator='\n').split('\n')

                    staff_info = info_text[0]
                    movie_details = info_text[1]

                    # 使用正则表达式解析导演和主演
                    director_match = re.search(r'导演:\s?(.*?)\s*(?:主演:|$)', staff_info)
                    director = director_match.group(1).strip() if director_match else 'N/A'

                    actors_match = re.search(r'主演:\s?(.*)', staff_info)
                    actors = actors_match.group(1).strip() if actors_match else 'N/A'

                    # 解析年份、国家、类型
                    details_parts = [part.strip() for part in movie_details.split('/')]
                    year = details_parts[0]
                    country = details_parts[1]
                    genres = '/'.join(details_parts[2].split())  # 类型可能有多个，用 / 拼接回去

                    print('director: ',director,", actors: ", actors,', year: ',year,', country: ',country,', genres: ',genres)

                    # 3. 获取评分和评价人数
                    rating = item.find('span', class_='rating_num').get_text(strip=True)
                    rating_count = 'N/A'

                    all_span = item.find_all('span')
                    for span in all_span:
                        text = span.get_text(strip=True)
                        if '人评价' in text:
                            rating_count = text[:-3]
                            break

                    print('rating: ',rating,', rating_count: ',rating_count)

                    # 4. 获取引言
                    quote_span = item.find('p', class_='quote')
                    quote = quote_span.get_text(strip=True) if quote_span else ''

                    print('quote: ',quote)

                    # 5. 组装成一个字典，方便写入CSV
                    movie_data = {
                        '排名': rank,
                        '标题': title,
                        '链接': link,
                        '导演': director,
                        '主演': actors,
                        '年份': year,
                        '国家': country,
                        '类型': genres,
                        '评分': rating,
                        '评价人数': rating_count,
                        '一句话评价': quote
                    }

                    # 写入一行数据到CSV
                    writer.writerow(movie_data)
                    rank += 1

            except requests.RequestException as e:
                print(f"请求页面失败: {e}")
            except Exception as e:
                print(f"在处理页面 {url} 时发生错误: {e}")

            # 延时1秒，防止IP被封
            time.sleep(1)

        print(f"\n豆瓣Top250相关数据爬取完成！数据已成功保存到 {csv_file_path} 文件中。")

except IOError as e:
    print(f"文件操作失败: {e}")