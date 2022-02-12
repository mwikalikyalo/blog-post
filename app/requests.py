from app import app
import urllib.request,json
from .models import Quotes

Quotes = quotes.quotes

# Getting api url
api_url = app.config['QUOTES_API_URL']

def get_quotes(id):
    '''
    Function that gets the json response to our url request
    '''
    get_quotes_url = api_url.format(id)

    with urllib.request.urlopen(get_quotes_url) as url:
        get_quotes_data = url.read()
        get_quotes_response = json.loads(get_quotes_data)

        quotes_results = None
        if get_quotes_response['results']:
            quotes_results_list = get_quotes_response['results']
            quotes_results = process_results(quotes_results_list)

    return quotes_results

def process_results(quotes_list):
    '''
    Function  that processes the movie result and transform them to a list of Objects
    '''
    quotes_results = []
    for quote_item in quotes_list:
        author = quote_item.get('author')
        id = quote_item.get('id')
        quote = quote_item.get('quote')

        if quote:
            quote_object = Quotes(author, id, quote)
            quotes_results.append(quote_object)

    return quotes_results