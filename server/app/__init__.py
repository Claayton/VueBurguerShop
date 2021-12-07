"""Diretório principal onde as instâncias do app são inicializadas"""
from flask import Flask

from app.extensions import database
from app.extensions import migrations

from .routes import teste
from .routes.ingredients import ingredients_routes

def minimal_app(config_file: dir):
    """
    Inicia um app básico para ser utilizado como base para instanciar tanto o app principal,
    quanto o app de testes.
    """
    app = Flask(__name__)
    app.config.from_object(config_file)
    return app

def create_app(config_file='config'):
    """Instancia do app principal."""
    app = minimal_app(config_file)

    database.init_app(app)
    migrations.init_app(app)

    app.register_blueprint(teste.bp)
    app.register_blueprint(ingredients_routes.bp)

    return app
