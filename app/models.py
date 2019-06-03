from werkzeug.security import generate_password_hash, check_password_hash
from datetime import date

from app import db


class User(db.Model):
    """
    Create an User table
    """

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256))
    email = db.Column(db.String(256), unique=True)
    password_hash = db.Column(db.String(256))
    


    @property
    def password(self):
        return self.password_hash
    
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User: {}>'.format(self.name)
