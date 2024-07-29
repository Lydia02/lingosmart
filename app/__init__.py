from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect

from flask_login import LoginManager
from flask_bcrypt import Bcrypt

db = SQLAlchemy()

app = Flask(__name__)



app.config['SECRET_KEY'] = 'you-will-never-guess'

# # mysql db to be connected to after everything is done
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://lingosmart:Oms%402002@lingosmart.mysql.pythonanywhere-services.com/lingosmart$user'


# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
csrf = CSRFProtect(app)
bcrypt = Bcrypt(app)
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)




from app import routes
