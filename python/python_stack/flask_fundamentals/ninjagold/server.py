from flask import Flask, render_template, request,redirect, url_for,session
app = Flask(__name__)
app.secret_key='123'

import random 
	

@app.route('/')
def index():
	if not 'gold' in session:
		session['gold'] = 0

	return render_template('index.html', gold=session['gold'])

@app.route('/process', methods=['POST'])
def process():
	
	
	if request.form['building'] == 'farm':
		session['gold'] = random.randrange(10,21)


	return redirect('/')

app.run(debug=True)