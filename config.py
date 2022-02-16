import os

class Config:
    '''
    General configuration parent class
    '''
    QUOTE_BASE_URL ='http://quotes.stormconsultancy.co.uk/random.json'
    SECRET_KEY= os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:0000@localhost/watchlist'
    UPLOADED_PHOTOS_DEST ='app/static/images'

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
    pass

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:0000@localhost/blog-post'
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}
