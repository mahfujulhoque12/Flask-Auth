from flask import Blueprint, render_template


auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template('login.html', boolean=False)

@auth.route('/logout')
def logout():
    return "<p>log out</p>"


@auth.route('/signup')
def sign_up():
    return render_template('sign_up.html')