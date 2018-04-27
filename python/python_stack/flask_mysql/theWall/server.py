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

@app.route('/register', methods=['POST'])
def result():

		first_name = request.form['first_name'],
		last_name = request.form['last_name'],
		email = request.form['email'],
		password = request.form['password']
		errors = False 

		if len(email) < 1:
			flash("email can't be empty!")
			errors = True 
		elif not EMAIL_REGEX.match(request.form['email']):
			flash("Invalid Email Address!")
			errors = True
		if len(first_name) < 1:
			flash("First name can't be empty!")
			errors = True
		elif not request.form['first_name'].isalpha():
			flash("first name cant contain any numbers")
			errors = True
		if len(last_name) < 1:
			flash("Last name can't be empty!")
			errors = True
		elif not request.form['last_name'].isalpha():
			flash("last name cant contain any numbers")
			erorrs = True
		if len(password) <= 8:
			flash("password must be more than 8 characters")
			errors = True
		if len(request.form['confirm']) < 1:
			flash("password can't be empty!")
			errors = True 
		if password != request.form['confirm']:
			flash("passwords do not match")
			errors = True
		
		if errors == True:
			return redirect('/')
		else:

			#query users for existing email address
			query = "SELECT * FROM users WHERE email = :email LIMIT 1"
			data = {
				'email': email
			}
			user = mysql.query_db(query,data)
			if len(user) > 0: #we have that email already
				flash('sorry email already taken')
				return redirect('/')
			else:	
				# run validations if they are all successful create password hash with bcrypt
				pw_hash = bcrypt.generate_password_hash(password)
				query = "INSERT INTO users(first_name, last_name, email, password,created_at, updated_at) Values(:first_name, :last_name, :email, :pw_hash,now(), now())"
				data = {
					'first_name':request.form['first_name'],
					'last_name': request.form['last_name'],
					'email': request.form['email'],
					'pw_hash': pw_hash
				}
				mysql.query_db(query,data)
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
		if len(user) > 0 : 
			if bcrypt.check_password_hash(user[0]['password'], password):
				#login user into session
				session['user_id'] = user[0]['id']
				return render_template('success.html')
			else:
				flash('Incorrect combination of email/password')
				return redirect('/')
		else:
			flash('Incorrect combo of email/password')
			return redirect('/')

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