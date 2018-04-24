from flask import Flask, request, redirect, render_template, session, flash,session
import re
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'emailvalid')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app.secret_key = "secret"

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/success', methods=['POST'])
def create():
	if not EMAIL_REGEX.match(request.form['email']):
		flash("EMAIL is not valid!")
		return redirect('/')
	else:
		query = "INSERT INTO email(email,created_at,updated_at) Values(:email, now(), now())"
		data = {
 			'email': request.form['email']
			}
		emails= mysql.query_db(query, data)
		
		return render_template('success.html', all_emails=emails)
	
app.run(debug=True)