from flask import Blueprint
from flask import render_template, request
from flask_login import login_required, current_user, logout_user

views = Blueprint('views', __name__)

@views.route('/')
def home():
    if current_user.is_authenticated:
        logout_user()
    return render_template('home.html')

@views.route('/userhome')
@login_required
def userhome():
    return render_template('userhome.html', user=current_user)