import unittest
from app.models import Blog, User
from app import db

class TestBlog(unittest.TestCase):
    def setUp(self):
        self.user_mwikali = User(username='mwikali', password ='potato', email = 'winniemwikali07@gmail.com')
        self.new_blog = Blog(title= 'Technology', content = 'Software development',user_id = self.user_mwikali.id)

    def tearDown(self):
        Blog.query.delete() 
        User.query.delete() 

    def test_check_instance_variables(self) :
        self.assertEquals(self.new_blog.title, 'Technology') 
        self.assertEquals(self.new_blog.content, 'Software development')  
        self.assertEquals(self.new_blog.user_id, self.user_mwikali.id)  

    def test_save_blog(self):
        self.new_blog.save_blog()  
        self.assertTrue(len(Blog.query.all())>0)  

    def test_get_pitch_by_id(self):
        self.new_blog.save_blog() 
        got_blog = Blog.get_blog(self.user_mwikali.id) 
        self.assertTrue(len(got_blog)==1) 