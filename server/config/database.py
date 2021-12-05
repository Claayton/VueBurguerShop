"""Diretório para ler configurações vindas das variáveis de ambiente"""
import os
from dotenv import load_dotenv

load_dotenv()

database_infos = {
    'secret_key': os.getenv('secret_key')
}
