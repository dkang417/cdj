from flask import Flask, render_template, request,redirect
app = Flask(__name__)

@app.route('/')
def index():
	return render_template("index.html", name ="bob")

@app.route('/users/<username>')
def show_user_profile(username):
	print username
	return render_template('user.html')


@app.route('/users', methods=['POST'])
def create_user():
	name = request.form['name']
	email = request.form['email']
	return render_template('/success.html')

app.run(debug=True)