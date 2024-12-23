from flask import Blueprint
from flask import render_template, request
from .models import User
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask import redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if(request.method == 'POST'):
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()
        if user:
            if check_password_hash(user.password, password):
                #login_user(user, remember=True)
                return redirect(url_for('views.userhome'))
            else:
                return render_template('login.html', password_error=True)
        else:
            return render_template('login.html', user_error=True)
    return render_template('login.html')

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if (request.method == 'POST'):
        firstname = request.form.get('name')
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()
        if user:
            return render_template('signup.html', exists_error=True)
        new_user = User(
            firstname=firstname, 
            username=username, 
            password=generate_password_hash(password, method='pbkdf2:sha256')
        )
        db.session.add(new_user)
        db.session.commit()
        return render_template('signup.html', created_user=True)
    
    return render_template('signup.html')