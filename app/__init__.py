# -*- coding: utf-8 -*-

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_login import LoginManager
import coverage
import os
import unittest


# Aplicativo
app = Flask(__name__)

# Configurações
app.config.from_object(os.environ['APP_SETTINGS'])

# Database
db = SQLAlchemy(app)

# Migrações
migrate = Migrate(app, db)

# Manager
manager = Manager(app)
manager.add_command('db', MigrateCommand)

# Autenticação

login = LoginManager(app)
login.login_view = 'login'

# Testes

@manager.command
def test():
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


@manager.command
def cov():
    cov = coverage.Coverage()

# Importações
from app import routes
from users import views, models

# Blueprints
app.register_blueprint(views.bp)

