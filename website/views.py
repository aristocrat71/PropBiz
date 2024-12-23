from flask import Blueprint
from flask import render_template, request

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('home.html')

@views.route('/userhome')
def userhome():
    return render_template('userhome.html')