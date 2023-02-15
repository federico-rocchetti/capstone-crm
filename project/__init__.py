import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# FLASK LOGIN
login_manager = LoginManager()

# FLASK APP
app = Flask(__name__)

app.config['SECRET_KEY'] = "devsecretkey"

# DATABASE
db = SQLAlchemy()

# FUNCTION TO CONNECT TO DATABASE
def connect_to_db(flask_app):

    flask_app.config["SQLALCHEMY_DATABASE_URI"] = os.environ["POSTGRES_URI"]
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = flask_app
    db.init_app(flask_app)

# FLASK LOGIN REQUIREMENTS
login_manager.init_app(app)
login_manager.login_view = "login"

