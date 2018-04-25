from flask import Flask, request, redirect, render_template, session, flash,session
import re
from mysqlconnection import MySQLConnector
import md5
app = Flask(__name__)
mysql = MySQLConnector(app,'loginAndregistration')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app.secret_key = "secret"



@app.route('/')
def index():                      
    return render_template('index.html') 

def create(request):
	first_name = request.form['first_name'],
	last_name = request.form['last_name'],
	email = request.form['email'],
	password = md5.new(request.form['password']).hexdigest()
	query = "INSERT INTO login(first_name, last_name, email, password,created_at, updated_at) Values(:first_name, :last_name, :email, :password,now(), now())"
	data = {
		'first_name':request.form['first_name'],
		'last_name': request.form['last_name'],
		'email': request.form['email'],
		'password': request.form['password']
	}

	mysql.query_db(query,data)

def display():
	query = "SELECT * FROM login"
	logins = mysql.query_db(query)
	return render_template('success.html', logins=logins)

@app.route('/success', methods=['POST'])
def result():
	
	if len(request.form['email']) < 1:
		flash("email can't be empty!")
		return redirect('/')
	elif not EMAIL_REGEX.match(request.form['email']):
		flash("Invalid Email Address!")
		return redirect('/')
	if len(request.form['first_name']) < 1:
		flash("First name can't be empty!")
		return redirect('/')
	if request.form['first_name'].isalpha() == False:
		flash("first name cant contain any numbers")
		return redirect('/')
	if len(request.form['last_name']) < 1:
		flash("Last name can't be empty!")
		return redirect('/')
	if request.form['last_name'].isalpha() == False:
		flash("last name cant contain any numbers")
		return redirect('/')
	if len(request.form['password']) <= 8:
		flash("password must be more than 8 characters")
		return redirect('/')
	if len(request.form['confirm']) < 1:
		flash("password can't be empty!")
		return redirect('/')
	if request.form['password'] != request.form['confirm']:
		flash("passwords do not match")
		return redirect('/')
	else:
		create(request)
		return display()

app.run(debug=True)