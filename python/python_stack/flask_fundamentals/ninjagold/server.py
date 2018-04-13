from flask import Flask, render_template, request,redirect, url_for,session
app = Flask(__name__)
app.secret_key='123'

import random 
	

@app.route('/') 
def index():
	

	if not 'gold' in session:
		session['gold'] = 0
	if not 'activities' in session:
		session['activities']=[]


	return render_template('index.html', gold=session['gold'],activities=session['activities'])

@app.route('/process', methods=['POST'])
def process():
	
	building = request.form['building']
	if building == 'farm':
	 	gold = random.randrange(10,21)
	 	session['activities'].append({'activity' :"you entered the {} and earned {} gold ".format(building,gold)})
		
	elif building == 'cave':
		gold = random.randrange(5,11)
		session['activities'].append({'activity' : "you entered the {} and earned {} gold ".format(building,gold)})
		

	elif building == 'house':
		gold = random.randrange(2,6)
		session['activities'].append({'activity' : "you entered the {} and earned {} gold ".format(building,gold)})
		

	elif building == 'casino':
		gold = random.randrange(-50,51)
		session['activities'].append({'activity' : "you entered the {} and earned {} gold ".format(building,gold)})
		

	session['gold'] += gold
	
	return redirect('/')

@app.route('/reset',methods=['POST']) 
def reset():
	session.pop('gold')
	session.pop('activities')
	return redirect('/')

app.run(debug=True)