from flask import Blueprint
from flask import render_template, request
from flask import flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    #if(request.method == 'POST'):
    data = request.form
    print(data)
    return render_template('login.html')

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if (request.method == 'POST'):
        firstname = request.form.get('name')
        username = request.form.get('username')
        password = request.form.get('password')

        print(firstname, username, password)
    return render_template('signup.html')