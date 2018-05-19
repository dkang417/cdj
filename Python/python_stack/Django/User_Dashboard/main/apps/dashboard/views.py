from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
import bcrypt 
from .models import *

# Create your views here.

def index(request):
	#protects our url from people not logged in
	if request.session.get('id') != None:
		return redirect('/dashboard')

	return render(request,'dashboard/index.html')

def register(request):
	if request.method == "POST":

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

			return redirect('/dashboard') 
	else: 
		return render(request,'dashboard/register.html')

def login(request):
	if request.method == "POST":

		email = request.POST['email']
		password = request.POST['password']
		user = User.objects.filter(email=email)
		#check to see if there is a matching user
		if len(user) > 0: 
			#we have a user so check password
			checkpassword = bcrypt.checkpw(password.encode(), user[0].password.encode())
			if checkpassword:
				request.session['id'] = user[0].id 
				return redirect('/dashboard')
		
			else:
				# right id but wrong password
				messages.error(request,'incorrect user/password combination.')
				return redirect('/login')
		else: 
			#user does not exist
			messages.error(request,'incorrect user/password combination')
			return redirect('/login')
	else: 
		return render(request,'dashboard/login.html')

def logout(request):
	request.session.clear()
	return redirect('/')

def dashboard(request):
	if request.session.get('id') == None:
		return redirect('/')

	context = {
			'user': User.objects.get(id=request.session['id'])
			
			}
	return render(request,'dashboard/dashboard.html', context)
