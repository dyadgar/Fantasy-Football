from sqlalchemy import ForeignKeyConstraint
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db,login_manager


class Users(UserMixin,db.Model):
    id = db.Column(db.Integer,primary_key=True, unique = True)
    email = db.Column(db.String(255),unique=True)
    username = db.Column(db.String(255),unique=True)
    password = db.Column(db.String(255))
    team = db.relationship('Team', backref='user', lazy='dynamic')

    def __repr__(self):
        return f'<Username: {self.username}>'

# class Login(db.Model):
#     login_id=db.Column(db.Integer,primary_key=True, unique=True)
#     user_id=db.Column(db.Integer,db.ForeignKey('users.user_id'))

@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))


class Players_db(db.Model):
    player_id = db.Column(db.Integer, primary_key=True, unique = True)
    name = db.Column(db.String(255), unique= True)
    number = db.Column(db.Integer, unique = True)
    position = db.Column(db.String(255))
    team_id = db.Column(db.Integer, db.ForeignKey('team.team_id'))


    def __repr__(self):
        return f'<Name: {self.name}>'


class Team(db.Model):
    team_id = db.Column(db.Integer, primary_key=True)
    team_name = db.Column(db.String(255), unique= True)
    tactic = db.Column(db.String(255))
    id = db.Column(db.Integer, db.ForeignKey('users.id'))
    player = db.relationship('Players_db', backref='team', lazy='dynamic')

