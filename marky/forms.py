from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, \
SelectField, FileField, BooleanField, HiddenField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms.fields.html5 import EmailField

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    verify_pw = PasswordField('Verify password', validators=[DataRequired(), EqualTo('password', message='Passwords must match!')])
    email = EmailField('Email address', [DataRequired(), Email()])
    submit = SubmitField('Sign up')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')