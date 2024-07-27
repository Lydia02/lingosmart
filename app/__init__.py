from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from flask_wtf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
import os

db = SQLAlchemy()

app = Flask(__name__)

def create_app():
    app = Flask(__name__)

    # Ensure the instance folder exists
    if not os.path.exists(os.path.join(os.getcwd(), 'instance')):
        os.makedirs(os.path.join(os.getcwd(), 'instance'))

    # Setting the database URI
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(app.instance_path, 'course.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize the database
    db.init_app(app)

    # Import models to register them with SQLAlchemy
    from app import models

    # Create the tables
    with app.app_context():
        db.create_all()

    return app

app.config['SECRET_KEY'] = 'you-will-never-guess'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
csrf = CSRFProtect(app)
bcrypt = Bcrypt(app)
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.login_view = 'login'




from app import routes
