import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')
    DEBUG = False

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:1234@localhost/hbnb_db'  
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Évite le warning inutile

config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}
