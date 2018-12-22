1# -*- coding: utf-8 -*-

from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from secrets import token_hex

class User(UserMixin, db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), nullable=False, unique=True)
    password_hash = db.Column(db.String(32), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    keys = db.relationship('KeySecret', backref='user', lazy='dynamic')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User: {}>'.format(self.username)


class KeySecret(db.Model):

    __tablename__ = 'keys'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    key_hash = db.Column(db.String)

    def __init__(self, *args, **kwargs):
        self.key_hash = self._generate_key_hash(16)

    def _generate_key_hash(self, nbytes):
        return token_hex(nbytes)

    def __repr__(self):
        return '<Key: {}>'.format(self.key_hash)


@login.user_loader
def user_loader(user_id):
    return User.query.get(int(user_id))

