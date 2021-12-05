"""Diretório de configurações do app"""
from config.database import database_infos

JSONIFY_PRETTYPRINT_REGULAR = True

SQLALCHEMY_DATABASE_URI = 'sqlite:///storage.sqlite3'
SQLALCHEMY_TRACK_MODIFICATIONS = True

SECRET_KEY = database_infos['secret_key']
