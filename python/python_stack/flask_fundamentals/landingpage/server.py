from flask import Flask, render_template, request,redirect
app = Flask(__name__)

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/ninja')
def ninja_profile():
	return render_template("ninja.html")

@app.route('/dojo/new')
def ninja_form():

	return render_template("dojo.html")

app.run(debug=True)