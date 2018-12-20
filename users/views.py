# -*- coding: utf-8 -*-

from flask import (
    Blueprint, render_template, redirect, url_for, flash, abort
)
from .forms import RegisterForm, LoginForm, RememberForm
from app import login, db
from flask_login import (
    current_user, login_required, logout_user, login_user
)
from .models import User

bp = Blueprint('users', 'users', template_folder='templates', url_prefix='/users')

@bp.route('/register', methods=['GET', 'POST'])
def register():

    'View de registro'

    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('users.login'))
    return render_template('register.html', title='Registro', form=form)


@bp.route('/login', methods=['GET', 'POST'])
def login():

    'View de login'

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is not None:
            login_user(user)
            return redirect(url_for('index'))
        flash('Usuário inexistente')
    return render_template('login.html', title='Login', form=form)


@bp.route('/logout')
@login_required
def logout():

    'View de logout'

    logout_user()
    return redirect(url_for('index'))


@bp.route('/remember', methods=['GET', 'POST'])
def remember():

    'View de esqueci a senha'

    form = RememberForm()
    return render_template('remember.html', title='Esqueci a senha', form=form)


@bp.route('/dashboard/<username>')
@login_required
def dashboard(username):

    'View de perfil do usuário'

    user = User.query.filter_by(username=username).first()
    return render_template('dashboard.html', title='Perfil', user=user)

