
from flask import Flask, render_template, request,redirect,session,flash
app = Flask(__name__)
app.secret_key = '123'
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


@app.route('/')
def index():
	return render_template("index.html")


@app.route('/users', methods=['POST'])
def create_user():
	email = request.form['email']
	fname = request.form['fname']
	lname = request.form['lname']
	password = request.form['password']
	confirm = request.form['confirm']
	if len(request.form['email']) < 1:
		flash("email can't be empty!")
	elif not EMAIL_REGEX.match(request.form['email']):
		flash("Invalid Email Address!")
	if len(request.form['fname']) < 1:
		flash("First name can't be empty!")
	if request.form['fname'].isalpha() == False:
		flash("first name cant contain any numbers")
	if len(request.form['lname']) < 1:
		flash("Last name can't be empty!")
	if request.form['lname'].isalpha() == False:
		flash("last name cant contain any numbers")
	if len(request.form['password']) <= 8:
		flash("password must be more than 8 characters")
	if len(request.form['confirm']) < 1:
		flash("password can't be empty!")
	if request.form['password'] != request.form['confirm']:
		flash("passwords do not match")
	else:
		flash("Thanks for submitting your information")

	return render_template('success.html', email=email,fname=fname, lname=lname,password=password,confirm=confirm)


app.run(debug=True)