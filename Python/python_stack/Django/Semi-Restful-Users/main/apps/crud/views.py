from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

from .models import User

# Create your views here.
def index(request):
	context = {
		"users" : User.objects.all()
	}	
	return render(request,'crud/index.html', context)

def new(request):
	return render(request, 'crud/add.html')

def create(request):
	if request.method == "POST":
		print request.POST

		User.objects.create(first_name=request.POST["first_name"], last_name=request.POST["last_name"],email=request.POST["email"])
		return redirect("/users")
	# elif request.method == "GET":
	
	# 	context = {
	# 		"users" : User.objects.all()
	# 	}
	# 	return render(request,"crud/index.html", context)
def delete(request,user_id):
	User.objects.get(id=user_id).delete()
	return redirect('/users')	
	
def edit(request,user_id):
	context = {
		"user": User.objects.get(id=user_id)
	}
	return render(request, "crud/edit.html", context)

def show_or_update(request,user_id):
	if request.method == "POST":
		user =User.objects.get(id=user_id) 
		user.first_name = request.POST["first_name"]
		user.last_name = request.POST["last_name"]
		user.email = request.POST["email"]
		user.save()
		return redirect('/users')
	else:
		context = {
			"user": User.objects.get(id=user_id)
		}
		return render(request, "crud/show.html", context)
