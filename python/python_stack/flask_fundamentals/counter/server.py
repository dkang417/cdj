
from flask import Flask, render_template, request,redirect,session
app = Flask(__name__)
app.secret_key='secret'



@app.route('/')
def index():
	if not "count" in session:
		session['count'] = 0
	return render_template("index.html", count=session['count'])


@app.route('/add', methods=['POST'])
def add_two():
	session['count'] += 2
	return redirect('/')

@app.route('/clear', methods=['POST'])
def clear():
	session['count'] = 0
	return redirect('/')

app.run(debug=True)