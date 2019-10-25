from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

Shifter = Flask(__name__)
Shifter.config.from_object(Config)
db = SQLAlchemy(Shifter)
login = LoginManager(Shifter)
login.login_view = 'Login'

from app import routes,models
