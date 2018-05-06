from django.shortcuts import render, HttpResponse, redirect
import random

def index(request):
	if request.session.get('gold') == None:
		request.session['gold'] = 0
	if request.session.get('activities') == None:
		request.session['activities']=[]

	context = {
		'gold' : request.session['gold'],
		'activities': request.session['activities']
	}
	return render(request,'ninjagold/index.html', context)



def process(request):
	
	building = request.POST['building']
	if building == 'farm':
	 	gold = random.randrange(10,21)
	 	request.session['activities'].append({'activity' :"you entered the {} and earned {} gold ".format(building,gold)})
		
	elif building == 'cave':
		gold = random.randrange(5,11)
		request.session['activities'].append({'activity' : "you entered the {} and earned {} gold ".format(building,gold)})
		

	elif building == 'house':
		gold = random.randrange(2,6)
		request.session['activities'].append({'activity' : "you entered the {} and earned {} gold ".format(building,gold)})
		

	elif building == 'casino':
		gold = random.randrange(-50,51)
		request.session['activities'].append({'activity' : "you entered the {} and earned {} gold ".format(building,gold)})
		

	request.session['gold'] += gold
	
	return redirect('/')

def reset(request):
	request.session.clear()
	return redirect('/')