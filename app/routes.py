from app import app, bcrypt, db
from app.forms import RegistrationForm, LoginForm, settingForm
from flask import render_template, jsonify, request, url_for, redirect
from app.models import User
from flask_login import login_user, current_user, logout_user, login_required


@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template("home.html")
@app.route("/login", methods=['GET', 'POST'])
def login():

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
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

        return redirect(url_for('login'))
    
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


@app.route('/kinyarwanda', methods=['GET', 'POST'])
def kinyarwanda():
    return render_template('kinyarwanda.html')

@app.route('/kinyarwanda_resource', methods=['GET', 'POST'])
def kinyarwanda_resource():
    return render_template('kinya_resource.html')

@app.route('/english', methods=['GET', 'POST'])
def english():
    return render_template('english.html')


@app.route('/english_resource', methods=['GET', 'POST'])    
def english_resource():
    return render_template('english_resource.html')

@app.route('/swahili', methods=['GET', 'POST'])
def swahili():
    return render_template('swahili.html')

@app.route('/swahili_resource', methods=['GET', 'POST'])
def swahili_resource():
    return render_template('swahili_resource.html')



@app.route('/resourses', methods=['GET', 'POST'])
def resourses():
    return render_template('resources.html')


@app.route('/french', methods=['GET', 'POST'])
def french():
    return render_template('french.html')


@app.route('/french_resource', methods=['GET', 'POST'])
def french_resource():
    return render_template('french_resource.html')


@app.route('/courses', methods=['GET', 'POST'])
def courses():  
    return render_template('course.html')


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    logout_user()
    return redirect(url_for('home'))




@app.route('/setting', methods=['GET', 'POST'])
@login_required
def setting():

    form = settingForm()

    

    if request.method == 'GET':

        form.first_name.data = current_user.first_name
        form.last_name.data = current_user.last_name
        form.email.data = current_user.email


    if form.validate_on_submit():
        current_user.first_name = form.first_name.data
        current_user.last_name = form.last_name.data
        current_user.email = form.email.data
        db.session.commit()
        return render_template('dashboard.html')


    return render_template('setting.html', form=form)


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
    
    