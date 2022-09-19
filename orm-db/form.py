from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,EqualTo

class Loginform(FlaskForm):
    username=StringField('User name',validators=[DataRequired('enter username')])
    password=PasswordField('Password',validators=[DataRequired('enter password')])
    submit=SubmitField('Login')

class RegisterForm(FlaskForm):
    username=StringField('User name',validators=[DataRequired('enter username')])
    password=PasswordField('Password',validators=[DataRequired('enter password'),EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Repeat Password',validators=[DataRequired('confirm password')])
    submit=SubmitField('Register')
