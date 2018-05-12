from django.shortcuts import render, HttpResponse, redirect

from django.contrib import messages

import bcrypt 
from .models import *

# Create your views here.
def index(request):
	if request.session.get('id') != None:
		return redirect('/success')

	return render(request,'loginandregister/index.html')

def register(request):
		errors = User.objects.basic_validator(request.POST)

		if len(errors):
			for tag, error in errors.iteritems():
				messages.error(request, error, extra_tags=tag)
				return redirect("/")
		else:
			first_name = request.POST["first_name"]
			last_name = request.POST["last_name"]
			email = request.POST["email"]
			password = request.POST["password"]
			hashed_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

			User.objects.create(first_name= first_name, last_name= last_name, email= email, password= hashed_pw)
			
			user = User.objects.get(email=email)
			
			request.session['id']= user.id

			messages.success(request,'Successfully Registered!')
			return redirect('/success') 

def success(request):
	if request.session.get('id') == None:
		return redirect('/')

	user = User.objects.get(id=request.session['id'])
	context = {'user': user}

	return render(request, 'loginandregister/success.html', context)

def login(request):
	email = request.POST['email']
	password = request.POST['password']
	user = User.objects.filter(email=email)
	#check to see if there is a matching user
	if len(user) > 0: 
		#we have a user so check password
		checkpassword = bcrypt.checkpw(password.encode(), user[0].password.encode())
		if checkpassword:
			request.session['id'] = user[0].id 
			messages.success(request, 'Successfully logged in!')
			return redirect('/success')
	
		else:
			# right id but wrong password
			messages.error(request,'incorrect user/password combination.')
			return redirect('/')
	else: 
		#user does not exist
		messages.error(request,'incorrect user/password combination')
		return redirect('/')

def logout(request):
	request.session.clear()
	return redirect('/')
