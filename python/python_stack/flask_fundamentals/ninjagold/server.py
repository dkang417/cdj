from flask import Flask, render_template, request,redirect, url_for,session
app = Flask(__name__)
app.secret_key='123'

import random 
	

@app.route('/')
def index():
	

	if not 'totalGold' in session:
		session['totalGold'] = 0

	if not 'farmGold' in session:
		session['farmGold'] = 0

	if not 'houseGold' in session:
		session['houseGold'] = 0

	if not 'caveGold' in session:
		session['caveGold'] = 0

	if not 'casinoGold' in session:
		session['casinoGold'] = 0


	return render_template('index.html', totalGold=session['totalGold'],caveGold=session['caveGold'], farmGold=session['farmGold'], houseGold=session['houseGold'], casinoGold=session['casinoGold'])

@app.route('/process', methods=['POST'])
def process():
	
	
	if request.form['building'] == 'farm':
	 	session['farmGold'] = random.randrange(10,21)
		session['totalGold'] = session['totalGold']+session['farmGold']
	elif request.form['building'] == 'cave':
		session['caveGold'] = random.randrange(5,11)
		session['totalGold']= session['totalGold'] + session['caveGold'] 
	elif request.form['building'] == 'house':
		session['houseGold'] = random.randrange(2,6)
		session['totalGold'] = session['totalGold'] + session['houseGold']
	elif request.form['building'] == 'casino':
		session['casinoGold'] = random.randrange(-50,50)
		session['totalGold'] = session['totalGold'] +session['casinoGold']
	
	return redirect('/')

app.run(debug=True)