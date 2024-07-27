from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app import create_app
import os

app = create_app()
app = Flask(__name__)

#Ensure the instance folder exists
if not os.path.exists(os.path.join(os.getcwd(), 'instance')):
    os.makedirs(os.path.join(os.getcwd(), 'instance'))

# Setting the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(app.instance_path, 'course.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Import models to register them with SQLAlchemy
# Move the import here to avoid circular import
from app import models

# Create the tables
with app.app_context():
    db.create_all()

@app.route('/')
def hello():
    return "Hello, this is the course database setup!"


if __name__ == '__main__':
    app.run()
    from app import app, db
    with app.app_context():
        db.create_all()

    app.run(debug=True)
