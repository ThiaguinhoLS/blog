# -*- coding: utf-8 -*-

from app import db

class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), nullable=False, unique=True)
    password = db.Column(db.String(32), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)

    def generate_password(self, value):
        pass

    def check_password(self, value):
        pass
