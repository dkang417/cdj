from flask import Flask, render_template, request,redirect,session,flash
app = Flask(__name__)
app.secret_key = '123'


@app.route('/')
def index():
	return render_template("index.html")


@app.route('/users', methods=['POST'])
def create_user():

	name = request.form['name']
	if len(request.form['name']) < 1:
		flash("Name can't be empty!")
	else: 
		flash("Success! your name is {}".format(request.form['name']))
	location = request.form['location']
	language = request.form['language']
	comment = request.form['comment']
	if len(request.form['comment']) < 1:
		flash("comment can't be empty!")
	elif len(request.form['comment']) > 120:
		flash("comments cant be longer than 120 words")
	else: 
		flash("Success! your comment is {}".format(request.form['comment']))
	return render_template('success.html', name=name, location=location,language=language,comment=comment)


app.run(debug=True)