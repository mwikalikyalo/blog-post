from flask import render_template
from . import auth

@auth.route('/signin')
def signin():
    return render_template('auth/signin.html')