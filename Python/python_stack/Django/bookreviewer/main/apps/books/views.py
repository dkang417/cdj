from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import *

# Create your views here.
def index(request):
    if "active_id" in request.session:
        return redirect('/books')
    return render(request, "books/index.html")

def register(request):
    User.objects.validate(request)
    return redirect("/")

def login(request):
    users = User.objects.filter(email=request.POST["email"])
    if len(users) > 0:
        user = users[0]
        if user.password == request.POST["password"]:
            request.session["active_id"] = user.id 
            return redirect('/books')
            #dashboard
    messages.error(request, "Invalid login information")
    return redirect("/")

def books(request):
	if request.session.get('active_id') == None:
		return redirect('/')
	
	context = {
		'user' : User.objects.get(id=request.session['active_id']),
		'books': Book.objects.all(),
		'reviews': Review.objects.all()
	}
	return render(request, 'books/books.html', context)

def logout(request):
	request.session.clear()
	return redirect('/')

def add(request):
	context = {
		'authors': Author.objects.all()
	}
	return render(request, 'books/add.html', context)

def addbook(request):
	if request.POST['author_write'] == '':
		author = Author.objects.get(id=request.POST['author_list'])
	else:
		author = Author.objects.create(name=request.POST['author_write'])

	title = request.POST['title']
	review = request.POST['content']
	rating = request.POST['rating']

	book = Book.objects.create(title=title, author = author)
	Review.objects.create(rating=rating, content = review, user=User.objects.get(id=request.session['active_id']), book = book)

	return redirect("/books/{}".format(book.id))

def showbook(request, id):
	# user = User.objects.filter(id=request.session['active_id'])
	book = Book.objects.get(id=id)
	reviews = Review.objects.filter(book=book)
	context = {
		'book': book,
		'reviews': reviews
	
	}

	return render(request, 'books/showbook.html', context)

