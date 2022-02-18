from crypt import methods
from flask import render_template,request,redirect,url_for,flash,abort
from . import main
from ..requests import get_quotes
from .forms import BlogForm, CommentsForm,UpdateProfile
from ..models import Comments, Blog, User
from flask_login import current_user, login_required
from .. import db,photos

@main.route('/')
def home():
    '''
    View root page function that returns the index page and its data
    '''
    # Getting quotes
    featured_quotes = get_quotes('quote')

    title = 'Quote of the hour.'
    return render_template('home.html', title = title, feature= featured_quotes)


@main.route('/user/comment/new/<int:id>', methods =["GET", "POST"])
def comment(id):
    form = CommentsForm()
    comments = Comments.query.filter_by(blog_id = id).all()
    blog = Blog.query.filter_by(id = id).first()

    if form.validate_on_submit():
        comment_submitted = form.comment.data
        new_comment = Comments(comment= comment_submitted, commenter = current_user, comments = blog )
        new_comment.save_comment()

    return render_template('comments.html', comment_form = form, comments = comments, blog = blog)
      

@main.route('/user/blog/new/<int:id>' , methods=["GET","POST"])
@login_required
def blog(id):
    form = BlogForm()
    blog = Blog.query.filter_by(id=id).first()

    if form.validate_on_submit():
        blog=Blog(title = form.title.data, content = form.content.data, blogger= current_user )      
        flash("Your blog has been published", "Success")
        return redirect(url_for('home'))
    return render_template("blog.html", title="New blog", blog=blog)


@main.route('/user/<full_name>')
def profile(full_name):
    user = User.query.filter_by(full_name = full_name).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)


@main.route('/user/<full_name>/update',methods = ['GET','POST'])
@login_required
def update_profile(full_name):
    user = User.query.filter_by(full_name = full_name).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('main.profile',full_name=user.full_name))

    return render_template('profile/update.html',form =form)


@main.route('/user/<full_name>/update/pic',methods= ['POST'])
@login_required
def update_pic(full_name):
    user = User.query.filter_by(full_name = full_name).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',full_name=full_name))