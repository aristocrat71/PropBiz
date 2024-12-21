from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

login_db = SQLAlchemy()

class UserLogin(login_db.Model, UserMixin):
    userid = login_db.Column(login_db.Integer, primary_key=True)
    password = login_db.Column(login_db.String(80))
