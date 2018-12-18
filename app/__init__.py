# -*- coding: utf-8 -*-
from flask import Flask

app = Flask(__name__)

from app import routes
from blueprints import users

app.register_blueprint(users.bp)

