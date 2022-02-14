from email.quoprimime import quote
from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_quotes
from .forms import CommentsForm
from ..models import Comments

@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    # Getting quotes
    featured_quotes = get_quotes('quote')
    print(featured_quotes)
    title = 'Quote of the hour.'
    return render_template('index.html', title = title, feature= featured_quotes)

# @main.route('/user/comment/new/<int:id>', methods =["GET", "POST"])
# @login_required
# def comment(id):
#     form = CommentsForm()
#     comments = Comments.query.filter_by(pitch_id = id).all()
#     blog = Blog.query.filter_by(id = id).first()

#     if form.validate_on_submit():
#         comment_submitted = form.comment.data
#         new_comment = Comments(comment= comment_submitted, commenter = current_user, comments = blog )
#         new_comment.save_comment()

#     return render_template('comments.html', comment_form = form, comments = comments, blog = blog)  
