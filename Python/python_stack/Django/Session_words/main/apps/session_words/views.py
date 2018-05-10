from django.shortcuts import render, HttpResponse, redirect
from time import strftime, localtime


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

	time = strftime("%I:%M %p, %b %d %Y", localtime())
	
	new_word = {
		'word': word,
		'color':color, 
		'font': font, 
		'time': time
		}
	request.session['words'].append(new_word)
	request.session.modified = True
	
	return redirect('/result')

def result(request):	
	return render(request, 'session_words/success.html')

def clear(request):
	request.session.clear()
	return redirect('/')
