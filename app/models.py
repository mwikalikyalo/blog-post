from . import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import login_manager
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
# class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255), unique = True, index = True)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String(255))
    pass_secure = db.Column(db.String(255))
    blog = db.relationship('Blog',backref = 'blogger',lazy = "dynamic")
    comments_id = db.relationship('Comments', backref = 'commenter', lazy ='dynamic')

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password) :
        self.pass_secure = generate_password_hash(password) 

    def verify_password(self,password):
        return check_password_hash(self.pass_secure, password)     

    def __repr__(self):
        return f'User{self.username}'

class Role(db.Model):
    __tablename__ = 'role'  

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User', backref ='role', lazy = 'dynamic')

    def __repr__(self):
        return f'User {self.name}'

class Comments(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key = True)
    comment = db.Column(db.String(255))
    blog_id = db.Column(db.Integer, db.ForeignKey('blog.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comment(cls, id) :
        comments = Comments.query.filter_by(blog_id = id).all()
        return comments 

class Blog(db.Model):
    __tablename__ = 'blog'

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(255))
    content = db.Column(db.String(255))
    date_posted = db.Column(db.DateTime,default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    comments_id = db.relationship('Comments', backref = 'comments', lazy ='dynamic')

    def save_blog(self):
        db.session.add(self)
        db.session.commit() 

    @classmethod    
    def get_blog (cls, id):
        blog = Blog.query.filter_by(user_id = id).all()
        return blog

class Quotes:
  def __init__(self,author, id, quote):
    self.author = author
    self.id = id
    self.quote = quote