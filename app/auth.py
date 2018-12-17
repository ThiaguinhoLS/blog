# -*- coding: utf-8 -*-

from flask import Blueprint, render_template

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/login')
def login():
    return 'Login Page'

