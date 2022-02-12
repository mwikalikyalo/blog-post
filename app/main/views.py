
from ..requests import get_quotes

@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    # Getting popular movie
    featured_quotes = get_quotes('popular')
    print(featured_quotes)
    title = 'Quote of the hour.'
    return render_template('index.html', title = title, feature= featured_quotes)