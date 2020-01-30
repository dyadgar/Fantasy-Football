from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail
import random



# Flask Object
app = Flask(__name__)
app.config['SECRET_KEY'] = random._urandom(56)
app.config['DEBUG'] = True
login_manager = LoginManager(app)
login_manager.init_app(app)
login_manager.login_view = 'login'


# Database Connetion \c
db_info = {'host': 'localhost',
           'database': 'football',
           'psw': 'asilos',
           'user': 'postgres',
           'port': '', }

app.config[
    'SQLALCHEMY_DATABASE_URI'] = f"postgres://{db_info['user']}:{db_info['psw']}@{db_info['host']}/{db_info['database']}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Database Representation
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import models,routes