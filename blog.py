# -*- coding: utf-8 -*-

from app import app, db
from users.models import User
from dotenv import load_dotenv
import os

# Adicona as variáveis de ambiente
dotenv_path = os.path.join(os.path.dirname(__file__), '.flaskenv')
load_dotenv(dotenv_path)


# Adiciona váriaveis ao contexto do shell
@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User}
