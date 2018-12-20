# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length


class RegisterForm(FlaskForm):

	'Formulário de registro'

	username = StringField(
		'Usuário', validators=[DataRequired(), Length(min=4, max=20)]
	)
	password = PasswordField(
		'Senha', validators=[DataRequired(), Length(min=8, max=20)]
	)
	confirm_password = PasswordField(
		'Confirma senha', validators=[DataRequired(), EqualTo('password')]
	)
	email = StringField('Email', validators=[DataRequired(), Email()])
	recaptcha = RecaptchaField()
	submit = SubmitField('Registrar-se')


class LoginForm(FlaskForm):

	'Formulário de login'

	username = StringField('Usuário', validators=[DataRequired()])
	password = PasswordField('Senha', validators=[DataRequired()])
	recaptcha = RecaptchaField()
	submit = SubmitField('Entrar')

	def validate_username(self, username):
		pass


class RememberForm(FlaskForm):

	'Formulário de esqueceu a senha'

	email = StringField('Email', validators=[DataRequired(), Email()])
	recaptcha = RecaptchaField()
	submit = SubmitField('Enviar')

	def validate_email(self, email):
		pass
