import flask_simplemde
from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, StringField , SelectField
from wtforms.validators import DataRequired

class CommentsForm(FlaskForm):
    comment = TextAreaField('Write your comment')
    submit = SubmitField('Submit')

class BlogForm(FlaskForm):
    title = StringField('Pitch title', validators=[DataRequired()])
    category = SelectField("Category", topics =[(1,'Technology'),(2,'Fitness'),(3,'Day in the life')],validators=[DataRequired()])
    content = TextAreaField('Write your blog', validators=[DataRequired()])
    submit = SubmitField('Submit') 