from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'friendsdb')
app.secret_key = "secret"
@app.route('/')
def index():
	query = "SELECT * FROM friends"
	friends = mysql.query_db(query)
	return render_template('index.html', all_friends=friends)

@app.route('/new', methods =["GET"])
def new():
	return render_template('add_friend.html')

@app.route('/new_friend', methods=["POST"])
def new_friend():
	query = "INSERT INTO friends(first_name, last_name, occupation, created_at, updated_at) Values(:first_name, :last_name, :occupation, now(), now())"
	data = {
		'first_name': request.form['first_name'],
		'last_name': request.form['last_name'],
		'occupation': request.form['occupation'],
	}
	mysql.query_db(query, data)
	flash("User Created!!")
	return redirect('/')

@app.route('/friends/<friend_id>')
def show(friend_id):
    query = "SELECT * FROM friends WHERE id = :specific_id"
    data = {'specific_id': friend_id}
    friends = mysql.query_db(query, data)
    return render_template('users.html', friends=friends[0])

@app.route('/friends/<friend_id>/update')
def update(friend_id):
	query = "SELECT * FROM friends WHERE id = :specific_id"
	data = {'specific_id': friend_id}
	friends = mysql.query_db(query, data)

	return render_template('edit.html',friends=friends)

@app.route('/friends/<friend_id>/edit', methods=['POST'])
def updatenow(friend_id):
	query = "UPDATE friends SET first_name = :first_name, last_name = :last_name, occupation =:occupation" 
	data = {'specific_id': friend_id}
	friends = mysql.query_db(query,data)
	return redirect('/',friends=friends)

@app.route('/friends', methods=['POST'])
def create():
	query = "INSERT INTO friends(first_name,last_name,occupation,created_at,updated_at) Values(:first_name, :last_name, :occupation, now(), now())"
	data = {
		'first_name': request.form['first_name'],
		'last_name': request.form['last_name'],
		'occupation': request.form['occupation']
	}
	mysql.query_db(query, data)
	return redirect('/')



@app.route('/friends/<friends_id>/destroy')
def delete(friends_id):
	query = "DELETE FROM friends WHERE id = :friends_id"
	data = {'friends_id': friends_id}
	mysql.query_db(query, data)
	return redirect('/') 



app.run(debug=True)