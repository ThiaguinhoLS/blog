# -*- coding: utf-8 -*-

from flask import Blueprint, render_template
from .forms import RegisterForm, LoginForm, RememberForm


bp = Blueprint('users', 'users', template_folder='templates', url_prefix='/users')

@bp.route('/register')
def register():
    form = RegisterForm()
    return render_template('register.html', title='Registro', form=form)


@bp.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)


@bp.route('/logout')
def logout():
    pass


@bp.route('/remember')
def remember():
    form = RememberForm()
    return render_template('remember.html', title='Esqueci a senha', form=form)

