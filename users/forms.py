# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo, Length


class RegisterForm(FlaskForm):

	'Formulário de registro'

	username = StringField(
		'Username', validators=[DataRequired(), Length(min=4, max=20)]
	)
	password = PasswordField(
		'Password', validators=[DataRequired(), Length(min=8, max=20)]
	)
	confirm_password = PasswordField(
		'Confirm password', validators=[DataRequired(), EqualTo('password')]
	)
	email = StringField('Email', validators=[DataRequired(), Email()])


class LoginForm(FlaskForm):

	'Formulário de login'

	username = StringField('Username', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()])

	def validate_username(username):
		pass


class RememberForm(FlaskForm):

	'Formulário de esqueceu a senha'

	pass
