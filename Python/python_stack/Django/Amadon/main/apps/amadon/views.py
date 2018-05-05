from django.shortcuts import render, HttpResponse, redirect


def index(request):
	
	return render(request,'amadon/index.html')

def process(request):
	print "success"

	if request.session.get('total_items') == None:
		request.session['total_items'] = 0
	if request.session.get('total_cost') == None:
		request.session['total_cost'] = 0
	
	cost = {
		'item1': '19.99',
		'item2': '29.99',
		'item3': '4.99',
		'item4': '49.99'
	}

	request.session['product_item'] = request.POST['product']
	request.session['product_cost'] = cost[request.POST['product']]
	request.session['product_quantity'] = request.POST['quantity']
	request.session['order_total'] = float(cost[request.POST['product']]) * int(request.POST['quantity'])

	request.session['total_items'] += int(request.POST['quantity'])
	request.session['total_cost'] += float(cost[request.POST['product']]) * int(request.POST['quantity'])
	
	return redirect('/result')


def result(request):	
	return render(request, 'amadon/success.html')

def goback(request):
	request.session.pop('product_item')
	request.session.pop('product_cost')
	request.session.pop('product_quantity')
	request.session.pop('order_total')
	return redirect('/')
