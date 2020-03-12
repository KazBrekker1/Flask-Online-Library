from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)
ENV = 'prod'

if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:egyboy777@localhost:5432/flaskLibrary'
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://ydaatekdcuuing:7aca1265747ade3ece7c4d60d86ad29ec34f717bc559411c0a78c4b574453f2f@ec2-52-73-247-67.compute-1.amazonaws.com:5432/ddmgbura88chg2'

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

app.config['SECRET_KEY'] = 'e6r5wf1rvbter89wfe65dv1bg'

# app.config['TESTING'] = False
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'Login'
login_manager.login_message_category = 'info'

from app import routs
