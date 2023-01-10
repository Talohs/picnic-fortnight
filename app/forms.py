from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField
from wtforms.validators import equal_to, input_required

class Signupform(FlaskForm):
    email = EmailField('Email', validators=[input_required()])
    username = StringField('Username', validators=[input_required()])
    password = PasswordField('Password', validators=[input_required()])
    confirm = PasswordField('Confirm Password', validators=[input_required(), equal_to('password')])
    submit = SubmitField()

