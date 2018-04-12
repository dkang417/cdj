from flask import Flask, render_template, request,redirect, url_for,session,Markup
app = Flask(__name__)
app.secret_key='123'

import random 



@app.route('/', methods=['GET','POST'])
def index():
	
	if session.get('randomNum') is None:
		session['randomNum'] = random.randrange(1,11)
	
	res = ""
	c = ""
	button = ""

	if request.method == 'POST':
		display = ""
		guess = int(request.form['guess'])
		
		if guess > session['randomNum']:
			res = "Too High"
			c = "red"
		elif guess < session['randomNum']:
			res = "Too Low"
			c = "red"
		elif guess == session['randomNum']:
			res = str(session['randomNum']) + " was the number!"
			c = "green"
			button = Markup('<a href="/restart" class="button">Play again!</a>')
			
	else:
		display = "hidden"
	return render_template('index.html', res=res, c=c, display=display,button=button )



@app.route('/restart')
def restart():
	session.pop('randomNum')
	return redirect('/')



app.run(debug=True)