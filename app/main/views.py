from crypt import methods
from operator import ne
from flask import render_template, abort, redirect, url_for, request, flash
from flask_login import current_user, login_required
from . import main
from ..email import mail_message
from ..models import User, Blog , Comments, Subscription
from .forms import SubscriptionForm, UpdateProfile, BlogForm , CommentsForm
from .. import db, photos
from ..requests import get_quotes


@main.route('/')
def home():
    '''
    View root page function that returns the index page and its data
    '''
    # Getting quotes
    featured_quotes = get_quotes('quote')
    blog = Blog.query.all()
    form = SubscriptionForm()
    if form.validate_on_submit():
        email = form.email.data
        new_subscriber = Subscription(email = email)
        new_subscriber.save_email()
        return redirect(url_for('main.index'))  

    title = 'Quote of the hour.'
    return render_template('home.html',  title = title, feature= featured_quotes, blog = blog, blogger = blog, form = form)
   
@main.route('/user/<fullname>') 
def profile(fullname):
    user = User.query.filter_by(fullname = fullname).first()
    blog = Blog.get_blog(user.id)
    if user is None:
        abort(404)

    return render_template('profile/profile.html',user = user, blog = blog ) 

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

        return redirect(url_for('.profile',fullname = user.fullname))

    return render_template('profile/update.html',form =form) 
    
@main.route('/user/<fullname>/update/pic', methods=['POST']) 
@login_required
def update_pic(fullname):
    user = User.query.filter_by(fullname = fullname).first() 
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()

    return redirect(url_for('main.profile',fullname=fullname))     

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
        for subsriber in subscribers:
            mail_message("New post alert", 'email/welcome_user', subsriber.email, user = current_user.fullname)
        return redirect(url_for('.home', fullname = current_user.fullname ))

    return render_template('new_blog.html', blog_form = form)

@main.route('/blog/<int:id>', methods =["GET", "POST"])
def single_blog(id):
    blog = Blog.query.filter_by(id = id). first()
    comments = Comments.query.filter_by(blog_id = id).all()

    return render_template('blog.html', blog = blog, comments = comments)

@main.route('/user/comment/new/<int:id>', methods =["GET", "POST"])
def comment(id):
    form = CommentsForm()
    blog = Blog.query.filter_by(id = id).first()

    if form.validate_on_submit():
        comment_submitted = form.comment.data
        new_comment = Comments(comment= comment_submitted, comments = blog )
        new_comment.save_comment()
        return redirect(url_for('.blog', id = id ))

    return render_template('new_comments.html', comment_form = form)

@main.route('/delete/blog/<int:id>')
def delete_blog(id):
    blog_to_delete = Blog.query.filter_by(id = id).first()
    
    db.session.delete(blog_to_delete)
    db.session.commit()
    return redirect(url_for('.profile', fullname = current_user.fullname, user = current_user ))   

@main.route('/delete/comment/<int:id>')
def delete_comment(id):
    comment_to_delete = Comments.query.filter_by(id = id).first()

    db.session.delete(comment_to_delete)
    db.session.commit()
    return redirect(url_for('.blog', id = comment_to_delete.blog_id ))    

@main.route('/blog/update/<int:id>', methods = ['GET', 'POST'])
def update(id):
    blog = Blog.query.filter_by(id = id).first() 
    form = BlogForm() 

    if form.validate_on_submit():
        blog.title = form.title.data
        blog.content = form.content.data
        db.session.add(blog)
        db.session.commit()
        return redirect(url_for('.blog', id = blog.id ))

    form.title.data = blog.title
    form.content.data = blog.content    

    return render_template('edits.html', form = form)

@main.route('/latest')
def latest()  :
    blogs = Blog.query.all()

    return render_template('recent.html', blogs = blogs) 