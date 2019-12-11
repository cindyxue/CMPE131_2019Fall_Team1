"""
FILE BEFORE IMPLEMENTING FACTORY METHOD FOR REFERENCE:

from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

Shifter = Flask(__name__)
Shifter.config.from_object(Config)
db = SQLAlchemy(Shifter)
login = LoginManager(Shifter)
login.login_view = 'login'
Shifter.secret_key = 'development key'



from app import routes,models
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login = LoginManager()

def create_app(test_config=None):
    
    Shifter = Flask(__name__)
    
    if test_config is None:
        from config import Config
        Shifter.config.from_object(Config)
    else:
        Shifter.config.from_mapping(test_config)
        
    db.init_app(Shifter)
    login.init_app(Shifter)
    login.login_view = 'login'
    Shifter.secret_key = 'development key'
    
    # all the pieces of the program
    with Shifter.app_context():
        from . import routes
        db.create_all()
    
    return Shifter
Shifter = create_app()
if __name__ == '__main__':
    Shifter.run()
