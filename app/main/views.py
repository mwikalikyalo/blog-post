from crypt import methods
from flask import render_template,request,redirect,url_for,flash,abort
from . import main
from ..requests import get_quotes
from .forms import BlogForm, CommentsForm,UpdateProfile
from ..models import Comments, Blog, User, Subscription
from flask_login import current_user, login_required
from .. import db,photos
from ..email import mail_message

@main.route('/')
def home():
    '''
    View root page function that returns the index page and its data
    '''
    # Getting quotes
    featured_quotes = get_quotes('quote')

    title = 'Quote of the hour.'
    return render_template('home.html', title = title, feature= featured_quotes)

#comment 
@main.route('/user/comment/new/<int:id>', methods=["GET", "POST"])
def comment(id):
    form = CommentsForm()
    comments = Comments.query.filter_by(blog_id = id).all()
    blog = Blog.query.filter_by(id = id).first()

    if form.validate_on_submit():
        comment_submitted = form.comment.data
        new_comment = Comments(comment= comment_submitted, commenter = current_user, comments = blog )
        new_comment.save_comment()

    return render_template('comments.html', comment_form = form, comments = comments, blog = blog)

@main.route('/delete/comment/<int:id>')
def delete_comment(id):
    comment_to_delete = Comments.query.filter_by(id = id).first()

    db.session.delete(comment_to_delete)
    db.session.commit()
    return redirect(url_for('blog.html', id = comment_to_delete.blog_id ))

# #new blog post 
@main.route('/user/blog/new', methods =['GET', 'POST'])
@login_required
def new_blog():
    form = BlogForm()
    subscribers = Subscription.query.all()

    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data
        new_pitch = Blog(title = title, content = content, blogger = current_user)
        new_pitch.save_blog()
        for subscriber in subscribers:
            mail_message("New post alert", 'email/welcome_user', subscriber.email, user = current_user.fullname)
        return redirect(url_for('main.profile', fullname = current_user.fullname ))

    return render_template('blog.html', blog_form = form)

@main.route('/delete/blog/<int:id>')
def delete_blog(id):
    blog_to_delete = Blog.query.filter_by(id = id).first()
    
    db.session.delete(blog_to_delete)
    db.session.commit()
    return redirect(url_for('main.profile', fullname = current_user.fullname, user = current_user ))   


# #profile
@main.route('/user/<fullname>')
def profile(fullname):
    user = User.query.filter_by(fullname = fullname).first()
    blogs = Blog.get_blog(user.id)
    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user, blogs = blogs)

@main.route('/user/<fullname>/update',methods = ['GET','POST'])
@login_required
def update_profile(fullname):
    user = User.query.filter_by(fullname = fullname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('main.profile',fullname = user.fullname))
    return render_template('profile/update.html',form =form)

@main.route('/user/<fullname>/update/pic',methods= ['POST'])
@login_required
def update_pic(fullname):
    user = User.query.filter_by(fullname = fullname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photos'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',fullname=fullname))