from flask import Flask, request, redirect, render_template, session, flash,session
from mysqlconnection import MySQLConnector
from flask_bcrypt import Bcrypt
import re
app = Flask(__name__)
bcrypt = Bcrypt(app)
mysql = MySQLConnector(app,'thewall')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app.secret_key = "secret"



@app.route('/')
def index():     
	return render_template('index.html') 
def create(request):
	first_name = request.form['first_name'],
	last_name = request.form['last_name'],
	email = request.form['email'],
	password = request.form['password']
	pw_hash = bcrypt.generate_password_hash(password)
	query = "INSERT INTO users(first_name, last_name, email, password,created_at, updated_at) Values(:first_name, :last_name, :email, :pw_hash,now(), now())"
	data = {
		'first_name':request.form['first_name'],
		'last_name': request.form['last_name'],
		'email': request.form['email'],
		'pw_hash': pw_hash
	}
	mysql.query_db(query,data)


@app.route('/register', methods=['POST'])
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
			flash("User Created!! Please Login")
			return redirect('/')

@app.route('/login', methods=['POST'])
def logged():
		email = request.form['email']
		password = request.form['password']
		query = "SELECT * from users WHERE email = :email LIMIT 1"
		data = {
			'email':email
		}
		user = mysql.query_db(query,data)
		if not user:
			flash("Please enter valid email.", 'login_error')
			return redirect('/')
		elif bcrypt.check_password_hash(user[0]['password'], password):
			session['user_id'] = user[0]['id']
			return render_template('success.html')
		else:
			flash('Invalid login', 'login_error')
			return render_template('index.html')

@app.route('/success', methods=['GET'])
def wall():
	query = 'SELECT users.first_name, users.last_name, messages.message, messages.id, messages.created_at FROM messages JOIN users ON messages.users_id=users.id'
   	comment_query = 'SELECT comments.users_id, comments.comment, comments.messages_id, users.first_name, users.last_name FROM comments INNER JOIN users ON users.id=comments.users_id INNER JOIN messages ON messages.id = comments.messages_id'
   	messages = mysql.query_db(query)
   	comments = mysql.query_db(comment_query)
   	return render_template('success.html', messages=messages, comments=comments)


@app.route('/makemessage', methods=['POST'])
def makemessage():
	data = {
		'currentsession': session['user_id'],
		'user_message': request.form['add_message']
	       }
   	query = 'INSERT INTO messages (users_id, message, created_at, updated_at) VALUES (:currentsession, :user_message, NOW(), NOW())'			
   	messages=mysql.query_db(query,data)
   	return redirect('/success')


@app.route('/makecomment/<id>', methods=['POST'])
def makecomment(id):
	data = {
		'specific_id': id,
		'currentsession': session['user_id'],
		'comment': request.form['add_comment']
		  }
	query = 'INSERT INTO comments (messages_id, users_id, comment, created_at, updated_at) VALUES (:specific_id, :currentsession, :comment, NOW(), NOW())'
	comments = mysql.query_db(query,data)
	return redirect('/success')

@app.route('/logout', methods=['POST'])
def logout():
	session.clear()
	return redirect('/')



app.run(debug=True)