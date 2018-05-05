from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime


def index(request):
	if request.session.get('words') == None:
		request.session['words'] = []

	return render(request,'session_words/index.html')

def process(request):
	print "success"

	word = request.POST['word']
	color = request.POST['color']

	if 'big_font' in request.POST:
		font = "big"
	else: 
		font = "normal"

	myDate = datetime.now()
	formatedDate = myDate.strftime("%Y-%m-%d %H:%M:%S")
	# dateandtime = datetime.strftime(datetime.now(), "%H:%M:%S %p, %B %d, %Y")

	request.session['words'].append({'word': word, 'color':color, 'font': font, 'formatedDate': formatedDate})
	request.session.modified = True
	
	return redirect('/result')

def result(request):	
	return render(request, 'session_words/success.html')

def clear(request):
	request.session.clear()
	return redirect('/')
