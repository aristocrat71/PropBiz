from . import db
from flask_login import UserMixin

class Property(db.Model):
    property_id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    name = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Integer, nullable=False)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(20), unique=True)
    password = db.Column(db.String(80))
    firstname = db.Column(db.String(20))
    property_id = db.relationship('Property')