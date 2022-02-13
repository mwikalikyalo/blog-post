from flask import Flask
from config import DevConfig

def create_app(config_name):
    """
    Function to create an app instance
    """
    # Initializing application
    app= Flask(__name__)

    # Setting up configuration
    app.config.from_object(DevConfig)
    app.config.from_pyfile('config.py')

from app import views