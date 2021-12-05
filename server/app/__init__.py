from flask import Flask
from .routes import teste

def minimal_app():
    app = Flask(__name__)
    return app

def create_app():
    app = minimal_app()
    
    app.register_blueprint(teste.bp)
    return app
