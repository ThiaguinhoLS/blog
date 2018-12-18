# -*- coding: utf-8 -*-

from flask import Blueprint, render_template

bp = Blueprint('users', __name__, url_prefix='/users')

@bp.route('/login')
def login():
    return render_template('auth/login.html')

