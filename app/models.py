class Quotes:

  def __init__(self,author, id, quote):
    self.author = author
    self.id = id
    self.quote = quote

class Comments(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key = True)
    comment = db.Column(db.String(255))
    blog_id = db.Column(db.Integer, db.ForeignKey('pitches.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comment(cls, id) :
        comments = Comments.query.filter_by(pitch_id = id).all()
        return comments 

class Blog(db.Model):
    __tablename__ = 'blog'

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(255))
    content = db.Column(db.String(255))
    date_posted = db.Column(db.DateTime,default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    comments_id = db.relationship('Comments', backref = 'comments', lazy ='dynamic')
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))

    def save_blog(self):
        db.session.add(self)
        db.session.commit() 

    @classmethod    
    def get_blog (cls, id):
        blog = Blog.query.filter_by(user_id = id).all()
        return blog
