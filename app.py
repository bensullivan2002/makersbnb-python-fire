import os
from flask import Flask, request, render_template, redirect
from lib.database_connection import get_flask_database_connection
from lib.user import *
from lib.user_repository import *

# Create a new Flask app
app = Flask(__name__)


# == Your Routes Here ==

# GET /index
# Returns the homepage
# Try it: open http://localhost:5001/index
@app.route('/index', methods=['GET'])
def get_index():
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
            return redirect(f"/index") # Should link to "successful sign up message with option to go to log in page but this needs to be worked on on HTML level"

    #NEED TO ADD FUNCTIONALITY TO CHECK IF EMAIL ALREADY IN DATABASE  
        






    
    


# These lines start the server if you run this file directly.
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
