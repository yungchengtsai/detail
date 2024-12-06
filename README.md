# DB-FinalProject

DB-FinalProject/
│
├── app/
│ ├── **init**.py # 初始化 Flask 應用
│ ├── models.py # 資料庫模型
│ ├── routes.py # 路由邏輯
│ └── forms.py # 表單處理
│
├── static/
│ ├── css/
│ │ └── main.css # 自定義樣式
│ ├── js/
│ │ └── main.js # 自定義腳本
│ └── images/ # 圖片資源
│
├── templates/
│ ├── base.html # 母版頁面
│ ├── home.html # 首頁
│ ├── login.html # 登入頁面
│ └── register.html # 註冊頁面
│
├── instance/
│ └── movie_database.db # SQLite 資料庫
│
├── config.py # 設定檔案
├── run.py # 啟動 Flask 應用
├── requirements.txt # Python 依賴項
└── README.md # 專案說明文件

資料庫內容查看可以下載 DB Browser for SQLite 開啟 instance 中的 movie_database
