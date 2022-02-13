from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Email

class SigninForm(FlaskForm):
  email = StringField('inputEmail3', validator=[DataRequired(), Email()])
  password = PasswordField('inputPassword3', validator=[DataRequired()])
  remember = BooleanField('remember me')
  submit= SubmitField('signin')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [DataRequired()])
    submit = SubmitField('Submit')