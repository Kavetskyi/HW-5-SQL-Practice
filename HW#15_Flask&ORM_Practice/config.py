class Config:
    DEBUG = True
    ENV = 'development'
    SQLALCHEMY_DATABASE_URI = "postgresql://yk_flask_orm:yk_flask_orm@db:5432/yk_flask_orm"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
