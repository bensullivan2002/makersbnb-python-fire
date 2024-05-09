import os
from flask import Flask, request, render_template, redirect, session
from flask_session import Session
from lib.database_connection import get_flask_database_connection

# Create a new Flask app
app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
# == Your Routes Here ==

# GET /index
# Returns the homepage
# Try it: open http://localhost:5001/index

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/login", methods=["POST", "GET"])
def login():
    return render_template("login.html")

@app.route("/login", methods=["POST", "GET"])
def login():
# if form is submited
	if request.method == "POST":
		# record the user name
		session["email"] = request.form.get("email")
        #session["password"] = request.form.get("password")
		# redirect to the main page
		return redirect("/spaces")
	return render_template("login.html")

@app.route("/")
def index():
# check if the users exist or not
	if not session.get("email"):
		# if not there in the session then redirect to the login page
		return redirect("/login")
	return render_template('spaces.html')

@app.route("/logout")
def logout():
	session["email"] = None
	return redirect("/")


# These lines start the server if you run this file directly.
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))

