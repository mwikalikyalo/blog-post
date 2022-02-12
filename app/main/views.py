from flask import Flask, render_template
from ..requests import get_quotes
from . import main

@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    # Getting quotes
    featured_quotes = get_quotes('quote')
    print(featured_quotes)
    title = 'Quote of the hour.'
    return render_template('index.html', title = title, feature= featured_quotes)