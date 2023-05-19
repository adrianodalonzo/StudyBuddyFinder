from flask import Blueprint, redirect, render_template, request, url_for
from werkzeug.security import check_password_hash, generate_password_hash

from ..objects.forms import LoginForm, SignupForm
from ..objects.user import User

auth_bp = Blueprint('auth', __name__, url_prefix='/auth/')

@auth_bp.route('/signup/')
def signup():
    form = SignupForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            hash = generate_password_hash(form.password.data)
            user = User(form.username.data, hash)
            # add user to db
        return redirect(url_for('home.home'))
    elif request.method == 'GET':
        return render_template('signup.html', form=form)

@auth_bp.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            return render_template('login.html', form=form)
        return redirect(url_for('home.home'))
    elif request.method == 'GET':
        return render_template('login.html', form=form)