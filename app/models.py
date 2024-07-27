from app import db, login_manager
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    instructor = db.Column(db.String(100), nullable=False)
    text_content = db.Column(db.Text, nullable=False)
    video_reference = db.Column(db.String(200), nullable=True)
    
    def __repr__(self):
        return f'<Course {self.name}>'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    img = db.Column(db.String(120), nullable=True, default="default.jpg")

    def __repr__(self):
        return '<User %r>' % self.email
