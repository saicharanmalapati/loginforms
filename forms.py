from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, SelectField, RadioField
from wtforms.validators import DataRequired
#app = Flask("__name__")


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    phone = IntegerField('Phone', validators=[DataRequired()])
    age = IntegerField('Age', validators=[DataRequired()])
    language = SelectField('Languages', choices=[('cpp', 'C++'),
                                                 ('py', 'Python')])
    Gender = RadioField('Gender', choices=[('M', 'Male'), ('F', 'Female')])

    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')
