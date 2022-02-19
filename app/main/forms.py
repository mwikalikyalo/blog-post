# import flask_simplemde
from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, StringField 
from wtforms.validators import DataRequired, Email
from flask_ckeditor import CKEditorField

class CommentsForm(FlaskForm):
    comment = CKEditorField('Comment', TextAreaField('Write your comment'), validators=[DataRequired()])
    submit = SubmitField('Submit')

class BlogForm(FlaskForm):
    title = StringField('Pitch title', validators=[DataRequired()])
    content = TextAreaField('Write your blog', validators=[DataRequired()])
    submit = SubmitField('Submit') 

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [DataRequired()])
    submit = SubmitField('Submit')

class SubscriptionForm(FlaskForm):
    email = email = StringField('Subscribe to be alerted when a new blog is posted', validators=[DataRequired(), Email()])
    submit = SubmitField('Submit')