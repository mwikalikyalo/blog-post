import unittest
from app.models import Pitches, User,Comments
from app import db

class CommentsTest(unittest.TestCase):
    def setUp(self):
        self.user_ruweydha = User(username='ruweydha', password ='potato', email = 'ruweydhaabdinoor@gmail.com')
        self.new_pitch = Pitches(title= 'Technology', content = 'Software development',user_id = self.user_ruweydha.id)
        self.new_comment = Comments(comment = 'You need to put more effort', pitch_id = self.new_pitch.id, user_id = self.user_ruweydha.id)

    def tearDown(self):
        Pitches.query.delete() 
        User.query.delete() 
        Comments.query.delete()

    def test_check_instance_variables(self) :
        self.assertEquals(self.new_comment.comment, 'You need to put more effort') 
        self.assertEquals(self.new_comment.pitch_id, self.new_pitch.id)  
        self.assertEquals(self.new_comment.user_id, self.user_ruweydha.id)  

    def test_save_pitch(self):
        self.new_comment.save_comment() 
        self.assertTrue(len(Comments.query.all())>0)  

    def test_get_comment_by_id(self):
        self.new_comment.save_comment() 
        got_comment = Comments.get_comment(self.new_pitch.id) 
        self.assertTrue(len(got_comment)==1) 