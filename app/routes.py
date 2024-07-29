from app import app, bcrypt, db
from app.forms import RegistrationForm, LoginForm
from flask import render_template, jsonify
from app.models import User


@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template("home.html")
@app.route("/login", methods=['GET', 'POST'])
def login():

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            return render_template("dashboard.html")


    return render_template("login.html", form=form)
@app.route("/reset", methods=['GET', 'POST'])
def reset():
    return render_template("reset.html")

@app.route("/signup", methods=['GET', 'POST'])
def signup():

    form = RegistrationForm()
    if form.validate_on_submit():
        
        existing_user = User.query.filter_by(email=form.email.data).first()

        if existing_user is not None:
            return render_template("signup.html", form=form)


        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(first_name=form.first_name.data, last_name=form.last_name.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()

        return render_template("login.html")
    
    return render_template("signup.html", form=form)


 
@app.route('/services', methods=['GET', 'POST'])
def services():
    return render_template('services.html')

@app.route('/aboutus', methods=['GET', 'POST'])
def aboutus():
    return render_template('aboutus.html')

@app.route('/contactus', methods=['GET', 'POST'])
def contactus():
    return render_template('contactus.html')

@app.route("/dashboard", methods=['GET', 'POST'])
def dashboard():
    return render_template('dashboard.html')










# APIs
#dummy
users = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"}
]
@app.route("/api/users", methods=['GET', 'POST'])
def get_users():
    #dummy for now
    return jsonify(users)

@app.route("/api/users/<int:id>", methods=['GET', 'POST'])
def get_user(id):
    for user in users:
        if user["id"] == id:
            return jsonify(user)
    
    