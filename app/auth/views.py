from flask import render_template
from . import auth

@auth.route('/signin')
def login():
    return render_template('auth/signin.html')