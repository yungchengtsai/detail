# run.py
from app import create_app, db
from app.models import User, Movie, Cinema, ScreeningTime
from datetime import datetime, timedelta

app = create_app()


def create_sample_data():
    # 檢查是否已經有數據
    if Movie.query.first() is not None:
        return

    # 創建電影
    movies = [
        Movie(
            title="復仇者聯盟4：終局之戰",
            description="漫威電影宇宙第22部作品，復仇者聯盟要從薩諾斯手中拯救宇宙。",
            genre="動作/科幻",
        ),
        Movie(
            title="星際大戰：天行者崛起",
            description="星際大戰系列最終章，蕾伊完成絕地訓練，對抗第一軍團。",
            genre="科幻/冒險",
        ),
        Movie(
            title="玩具總動員4",
            description="胡迪和巴斯光年展開全新冒險，尋找新主人的玩具。",
            genre="動畫/冒險",
        ),
    ]

    # 創建影院
    cinemas = [
        Cinema(name="大都會影城", location="台北市信義區"),
        Cinema(name="新光影城", location="台北市西門町"),
        Cinema(name="威秀影城", location="台北市信義區"),
    ]

    # 添加到數據庫
    for movie in movies:
        db.session.add(movie)
    for cinema in cinemas:
        db.session.add(cinema)

    # 提交以獲取ID
    db.session.commit()

    # 創建放映時間
    current_date = datetime.now()
    for movie in movies:
        for cinema in cinemas:
            # 為每部電影在每個影院安排未來7天的放映場次
            for day in range(7):
                screening_date = current_date + timedelta(days=day)
                # 每天3個時段
                times = [
                    screening_date.replace(hour=14, minute=30),
                    screening_date.replace(hour=17, minute=30),
                    screening_date.replace(hour=20, minute=30),
                ]
                for time in times:
                    screening = ScreeningTime(
                        movie_id=movie.id, cinema_id=cinema.id, date=time
                    )
                    db.session.add(screening)

    # 創建一個管理員帳號
    admin = User(username="admin", email="admin@example.com")
    admin.set_password("admin123")
    db.session.add(admin)

    db.session.commit()


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        create_sample_data()  # 創建示例數據
    app.run(debug=True, host='0.0.0.0', port=5000)
