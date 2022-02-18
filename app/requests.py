from cgi import print_directory
from email.quoprimime import quote
import urllib.request,json
from .models import Quotes

Quotes = quote

# Getting the movie base url
base_url = None

def configure_request(app):
    global base_url
    base_url = app.config['QUOTE_BASE_URL']

def get_quotes(id):
    '''
    Function that gets the json response to our url request
    '''
    get_quotes_url = base_url.format(id)

    with urllib.request.urlopen(get_quotes_url) as url:
        get_quotes_data = url.read()
        get_quotes_response = json.loads(get_quotes_data)
               
        return get_quotes_response 


