from django.shortcuts import render, HttpResponse, redirect


def index(request):
	return render(request,'survey/index.html')


def result(request):	
	return render(request, 'survey/success.html')

def process(request):
	if not 'counter' in request.session:
		request.session['counter'] = 1
	else:
		request.session['counter'] += 1

	request.session['name'] = request.POST['name']
	request.session['location'] = request.POST['location']
	request.session['language'] = request.POST['language']
	request.session['comment'] = request.POST['comment']

	return redirect('/result')


	


