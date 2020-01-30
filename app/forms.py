from flask_wtf import FlaskForm
from wtforms.validators import data_required, Length, Email
from wtforms import StringField, SubmitField,PasswordField,BooleanField,IntegerField,SelectField

class RegistrationForm(FlaskForm):
    username= StringField('User Name', validators=[data_required()])
    password= PasswordField('Password', validators=[data_required(), Length(min=5, max=20)])
    email= StringField('Email   ', validators=[data_required(),Email()])
    submit= SubmitField('Register')

class LoginForm(FlaskForm):
    username= StringField('User Name', validators=[data_required()])
    password= PasswordField('Password', validators=[data_required(), Length(min=5, max=20)])
    # remember = BooleanField('Remember me')
    submit= SubmitField('Sign In')

class PlayerForm(FlaskForm):
    name= StringField('Player Name', validators=[data_required()])
    number= IntegerField('Player Number', validators=[data_required()])
    position= SelectField('Player Position', choices=[('gk','GK'),('df','DF'),('mf','MF'),('fw','FW')])
    submit=SubmitField('Save Configuration')


class TeamForm(FlaskForm):
    team_name = StringField('Team Name', validators=[data_required()])
    tactic=SelectField('Tactics', choices=[('4-4-2','4-4-2'),('4-3-3','4-3-3'),('5-3-2','5-3-2')])
    submit=SubmitField('Create Your Team')

# class Config(FlaskForm):
