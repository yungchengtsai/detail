from datetime import datetime, timedelta
from app import db
from app.models import User, Movie, Cinema, ScreeningTime

def seed_movies():
    """創建電影數據"""
    return [
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

def seed_cinemas():
    """創建影院數據"""
    return [
        Cinema(name="大都會影城", location="台北市信義區"),
        Cinema(name="新光影城", location="台北市西門町"),
        Cinema(name="威秀影城", location="台北市信義區"),
    ]

def create_screening_times(movies, cinemas):
    """創建放映時間"""
    screenings = []
    current_date = datetime.now()
    for movie in movies:
        for cinema in cinemas:
            for day in range(7):
                screening_date = current_date + timedelta(days=day)
                times = [
                    screening_date.replace(hour=14, minute=30),
                    screening_date.replace(hour=17, minute=30),
                    screening_date.replace(hour=20, minute=30),
                ]
                for time in times:
                    screenings.append(
                        ScreeningTime(
                            movie_id=movie.id,
                            cinema_id=cinema.id,
                            date=time
                        )
                    )
    return screenings

def create_admin():
    """創建管理員帳號"""
    admin = User(username="admin", email="admin@example.com")
    admin.set_password("admin123")
    return admin

def init_db():
    """初始化數據庫"""
    # 檢查是否已有數據
    if Movie.query.first() is not None:
        return
    
    # 創建並添加數據
    movies = seed_movies()
    cinemas = seed_cinemas()
    
    db.session.add_all(movies)
    db.session.add_all(cinemas)
    db.session.commit()
    
    # 創建放映時間
    screenings = create_screening_times(movies, cinemas)
    db.session.add_all(screenings)
    
    # 創建管理員
    admin = create_admin()
    db.session.add(admin)
    
    db.session.commit()
