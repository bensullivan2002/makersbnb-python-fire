import os

from flask import Flask, request, render_template, redirect, session
from lib.database_connection import get_flask_database_connection
from lib.user import *
from lib.user_repository import *

# Create a new Flask app
app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
# == Your Routes Here ==

# GET /index
# Returns the homepage
# Try it: open http://localhost:5001/index

app.secret_key = b'secret_key_to_be_changed'

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/index', methods=['POST'])
def signup_user():
    connection = get_flask_database_connection(app)
    user_repository = UserRepository(connection)
    email = request.form['email']
    password = request.form['password']
    confirm_password = request.form['confirm_password']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    phone_number = request.form['phone_number']
    if password != confirm_password:
        error_message = "Passwords don't match!"
        return render_template('index.html', error_message=error_message)
    if password == confirm_password:
        user = User(None, email, password, first_name, last_name, phone_number)
        errors = user.generate_errors()
        if errors:
            return render_template('index.html', errors=errors)
        else:
            user_repository.create(user)
            return redirect(f"/login") 

    #NEED TO ADD FUNCTIONALITY TO CHECK IF EMAIL ALREADY IN DATABASE  
        
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        if not session:
            return render_template("login.html")
        session.pop('user_fullname', None)
        session['logged_in'] = False
        return render_template('login.html')
    if request.method == 'POST':
        connection = get_flask_database_connection(app)
        user_repository = UserRepository(connection)
        email = request.form['email'] 
        password = request.form['password']
        user = user_repository.find_user_from_email(email)
        if user and password == user.password:
            session['logged_in'] = True
            session['user_fullname'] = f'{user.first_name} {user.last_name}'
            session['user_id'] = user.id # Angelicas request
            return redirect('/spaces') 
        return 'Invalid username or password'

@app.route('/spaces', methods=['GET'])
def view_spaces():
    if not session:
        return render_template('login.html')
    if session['logged_in']:
        fullname = session['user_fullname']
        return render_template('spaces.html', fullname=fullname)
    return render_template('login.html') 

if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))

