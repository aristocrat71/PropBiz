from . import db
from flask_login import UserMixin

class Property(db.Model):
    property_id = db.Column(db.Integer, primary_key=True)
    owner_name = db.Column(db.String(20), db.ForeignKey('user.username'))
    name = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Integer, nullable=False)

class User(db.Model, UserMixin):
    username = db.Column(db.String(20), primary_key=True)
    password = db.Column(db.String(80))
    firstname = db.Column(db.String(20))
    property_id = db.relationship('Property')