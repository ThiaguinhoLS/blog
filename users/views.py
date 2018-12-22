# -*- coding: utf-8 -*-

from flask import (
    Blueprint, render_template, redirect, url_for, flash, abort, current_app
)

from app import login, db
from flask_login import (
    current_user, login_required, logout_user, login_user
)
from flask_mail import Message
from .models import User, KeySecret
from .forms import RegisterForm, LoginForm, RememberForm, ChangePasswordForm
from app.email import send_email

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
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None:
            key_secret = KeySecret(user=user)
            db.session.add(key_secret)
            db.session.commit()
            send_email(
                subject='Esqueci a senha',
                sender=current_app.config['ADMIN'],
                recipients=[user.email],
                text_body=render_template(
                    'remember_password.txt', key_secret=key_secret, user=user
                ),
                html_body=render_template(
                    'remember_password.html', key_secret=key_secret, user=user
                )
            )
            flash('Uma chave de segurança foi enviada ao email informado')
            return redirect(url_for('index'))
        else:
            flash('Usuário inexistente', category='error')
    return render_template('remember.html', title='Esqueci a senha', form=form)


@bp.route('/dashboard/<username>')
@login_required
def dashboard(username):

    'View de perfil do usuário'

    user = User.query.filter_by(username=username).first()
    return render_template('dashboard.html', title='Perfil', user=user)


@bp.route('/change-password/<key_secret>/<username>', methods=['GET', 'POST'])
def change_password(key_secret, username):
    key_secret = KeySecret.query.filter_by(key_hash=key_hash).first()
    if key_secret and key_secret.user.username == username:
        form = ChangePasswordForm()
        if form.validate_on_submit():
            user = User.query.filter_by(username=username).first()
            user.set_password(form.password.data)
            db.session.commit()
            flash('Senha alterada com sucesso')
            return render_template('index')
        return render_template('change_password.html', form=form)
    return abort(400)

