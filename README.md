# Recommender_System
电影推荐系统

Recommender_System/
├── .git/
├── .idea/                 # (被.gitignore忽略)
├── .venv/                 # (被.gitignore忽略)
├── data/                  # 存放爬虫生成的CSV文件
│   ├── books.csv
│   └── douban_top250_movies.csv
├── scrapers/              # 存放所有的爬虫脚本
│   ├── douban_crawler.py
│   └── web_crawler.py
├── django_project/        # 存放所有的Django代码
│   ├── config/            # Django项目配置 (原config文件夹)
│   │   ├── __init__.py
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── manage.py          # Django管理脚本
│   └── ...                # Django app会放在这里
├── .gitignore
└── README.md
