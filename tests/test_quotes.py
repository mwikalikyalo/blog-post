from email.quoprimime import quote
import unittest
from models import Quotes

Quotes = quote

class QuoteTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Movie class
    '''
    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_quote = Quotes('Khaled Hosseini',28,'Nothing lasts forever')
    def test_instance(self):
        self.assertTrue(isinstance(self.new_quote,Quotes))


if __name__ == '__main__':
    unittest.main()