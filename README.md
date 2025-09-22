# Recommender_System (电影推荐系统)

## 项目目录结构
```
Recommender_System/
├── .git/ # Git 版本控制
├── .idea/ # IDE 配置 (已忽略)
├── .venv/ # 虚拟环境 (已忽略)
├── data/ # 存放爬虫生成的CSV文件
│ ├── movies_.csv
│ ├── reviews_.csv
│ └── ...
├── scrapers/ # 爬虫脚本
│ ├── new_crawler.py # 豆瓣热门电影 & 评论爬虫
│ ├── test_new_crawler.py # 爬虫测试脚本
│ └── ...
├── algorithm/ # 算法
│ └── Truth_value.py # 数据清洗 & 真值生成
├── django_project/ # Django Web 项目
│ ├── config/ # Django 配置文件
│ │ ├── init.py
│ │ ├── asgi.py
│ │ ├── settings.py
│ │ ├── urls.py
│ │ └── wsgi.py
│ ├── manage.py # Django 管理脚本
│ ├── films_recommender_system # 推荐系统 app(定义了数据库，模型配置了基础API接口)
│ └── movie_frontend # 推荐系统 app(使用Django模板渲染前端页面)
├── truth_value_out/ # 真值算法输出 
│ ├── item_quality.csv
│ ├── interactions_gt.csv
│ ├── splits.csv
│ └── eval_samples.csv
├── requirements.txt # 项目依赖
├── .gitignore
└── README.md
```