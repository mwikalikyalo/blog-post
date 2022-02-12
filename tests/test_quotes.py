from email.quoprimime import quote
import unittest
from models import Quotes

Quotes = quote.quote

class QuoteTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Movie class
    '''
    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_quote = Quotes(1234,'Python Must Be Crazy','A thrilling new Python Series','https://image.tmdb.org/t/p/w500/khsjha27hbs',8.5,129993)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_quote,Quotes))


if __name__ == '__main__':
    unittest.main()