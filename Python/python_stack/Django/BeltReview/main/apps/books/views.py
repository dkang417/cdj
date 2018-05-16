from django.shortcuts import render, HttpResponse, redirect

from django.contrib import messages

import bcrypt 
from .models import *

# Create your views here.
def index(request):
	#protects our url from people not logged in
	if request.session.get('id') != None:
		return redirect('/books')

	return render(request,'books/index.html')


def register(request):
		errors = User.objects.basic_validator(request.POST)

		if len(errors):
			for tag, error in errors.iteritems():
				messages.error(request, error, extra_tags=tag)
				return redirect("/")
		else:
			name = request.POST["name"]
			alias = request.POST["alias"]
			email = request.POST["email"]
			password = request.POST["password"]
			hashed_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

			User.objects.create(name= name, alias= alias, email= email, password= hashed_pw)
			
			user = User.objects.get(email=email)
			
			request.session['id']= user.id

			messages.success(request,'Successfully Registered!')
			return redirect('/books') 
def books(request):
	if request.session.get('id') == None:
		return redirect('/')

	user = User.objects.get(id=request.session['id'])
	context = {'user': user}

	return render(request, 'books/books.html', context)

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
			return redirect('/books')
	
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

# def processreview(request):
# 	return redirect('/add')

def add(request, id): 
	book_title = request.POST["book_title"]
	book_author= request.POST["book_author"]
	book_review = request.POST["book_review"]
	book_rating = request.POST["book_rating"]

	author = Author.objects.create(author= book_author)
	book = Book.objects.create(title= book_title, author = author)
	Review.objects.create(comment= book_review, rating= book_rating, book=book, user=User.objects.get(id=request.session['id']))
	

	return redirect('books/{}'.format(id))

def booksadd(request):
	return render(request, 'books/booksadd.html')

def bookpage(request):
	return render(request, 'books/showbookreview.html')
