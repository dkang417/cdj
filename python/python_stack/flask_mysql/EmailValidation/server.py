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


def create(request):
	query = "INSERT INTO email(email,created_at,updated_at) Values(:email, now(), now())"
	data = {
 			'email': request.form['email']
		}
	mysql.query_db(query, data)

def display():
	query = "SELECT * FROM email"
	emails = mysql.query_db(query)
	return render_template('success.html',emails=emails)


@app.route('/success', methods=['POST'])
def result():
	if not EMAIL_REGEX.match(request.form['email']):
		flash("EMAIL is not valid!")
		return redirect('/')
	else:
		flash("the email you entered is a valid email address. Thank you!")
		create(request)
		return display()

app.run(debug=True)