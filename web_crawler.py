import requests
from bs4 import BeautifulSoup
import csv
import time

# 目标URL
url = 'http://books.toscrape.com/'

# 1. 发送HTTP GET请求
# 查询并添加headers模拟浏览器访问
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36 Edg/139.0.0.0'
}

try:
    response = requests.get(url, headers=headers)
    # 检查请求是否成功
    response.raise_for_status()  # 请求失败，抛出异常

    # 2. 解析HTML内容
    soup = BeautifulSoup(response.text, 'html.parser')

    # 3. 提取数据
    # 定位到所有书籍的容器。通过浏览器开发者工具分析，发现每本书都在一个 <article class="product_pod"> 标签里
    books = soup.find_all('article', class_='product_pod')

    # 准备一个列表来存储所有书籍的信息
    book_list = []

    for book in books:
        # 在每个书籍容器内，提取标题和价格
        # 标题在 h3 > a 标签的 title 属性里
        title = book.h3.a['title']

        # 价格在 <p class="price_color"> 标签的文本里
        price = book.find('p', class_='price_color').text

        # 将提取的信息存入字典
        book_info = {
            'title': title,
            'price': price
        }
        book_list.append(book_info)
        print(f"找到书籍: {title}, 价格: {price}")

    # 4. 存储数据到CSV文件
    # 定义CSV文件的表头
    fieldnames = ['title', 'price']

    with open('books.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # 写入表头
        writer.writeheader()

        # 写入书籍数据
        writer.writerows(book_list)

    print("\n数据已成功保存到 books.csv 文件中")

except requests.exceptions.RequestException as e:
    print(f"请求错误: {e}")
except Exception as e:
    print(f"发生未知错误: {e}")