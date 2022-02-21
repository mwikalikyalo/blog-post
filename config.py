import os

class Config:
    '''
    General configuration parent class
    '''
    QUOTE_BASE_URL ='http://quotes.stormconsultancy.co.uk/random.json'
    SECRET_KEY= os.environ.get('SECRET_KEY') or 'Quota'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:0000@localhost/blog_post'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True

    #email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:0000@localhost/blog_test'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:0000@localhost/comments_test'

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL').replace("://", "ql://", 1)
    
class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:0000@localhost/blog_post'
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}
