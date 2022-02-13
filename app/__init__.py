from flask import Flask
from config import DevConfig, config_options
from .main import main as main_blueprint

def create_app(config_name):
    """
    Function to create an app instance
    """
    # Initializing application
    app= Flask(__name__)

    # Creating the app configurations
    app.config.from_object(config_options[config_name])
    app.config.from_object(DevConfig)
    app.config.from_pyfile('config.py')

    # Registering the blueprint
    app.register_blueprint(main_blueprint)

    # setting config
    from .requests import configure_request
    configure_request(app)

from app import views