from flask import Flask
from flask_session import Session
from .config import AppConfig


def create_app():
    app = Flask(__name__)
    app.config.from_object(AppConfig)
    Session(app)

    from .routes import init_routes
    init_routes(app)

    return app
