from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'fullfriends')

@app.route('/')
def index():
	query = "select friends.name, friends.age, DATE_FORMAT(friends.created_at, '%M') as 'month',DATE_FORMAT(friends.created_at, '%D') as 'day', DATE_FORMAT(friends.created_at, '%Y') as 'year' from friends"
	friends = mysql.query_db(query)
	return render_template('index.html', all_friends=friends)



@app.route('/friends', methods=['POST'])
def create():
	query = "INSERT INTO friends(name,age,created_at,updated_at) Values(:name,  :age, now(), now())"
	data = {
		'name': request.form['name'],
		'age': request.form['age']
	}
	mysql.query_db(query, data)
	return redirect('/')
app.run(debug=True)