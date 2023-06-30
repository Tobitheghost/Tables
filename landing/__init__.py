from flask import Flask
from os import path
def create_app():
    app = Flask(__name__)

    from .portfolio import landingPage
    app.register_blueprint(landingPage, url_prefix='/')
    return app
