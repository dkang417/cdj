from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import *
import bcrypt

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
        password = request.POST['password']
        newPassword = bcrypt.checkpw(password.encode(), user.password.encode())
        if newPassword: 
            request.session["active_id"] = user.id 
            return redirect('/books')
         
    messages.error(request, "Invalid login information")
    return redirect("/")

def books(request):
	if request.session.get('active_id') == None:
		return redirect('/')

	context = {
		'user' : User.objects.get(id=request.session['active_id']),
		'books': Book.objects.all(),
		'recent_reviews':Review.objects.all().order_by('-created_at')[:3]
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
	if request.method == "POST":
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
	else:
		return redirect('/')
def showbook(request, id):
	book = Book.objects.get(id=id)
	reviews = Review.objects.filter(book=book)
	context = {
		'book': book,
		'reviews': reviews
	}

	return render(request, 'books/showbook.html', context)
def getuser(request):

	return redirect("/users/{}".format(user.id))

def showusers(request, id):
	user = User.objects.get(id=id)
	book = Book.objects.get(id=id)
	reviews = Review.objects.filter(book=book)
	total_reviews= len(user.reviews.all())
	reviewed_books = Review.objects.filter(user=user).values_list('book_id', 'content').distinct()
	


	context = {
		'user': user,
		'reviews': reviews,
		'total_reviews': total_reviews,
		'reviewed_books': reviewed_books
	}
	return render( request, 'books/showusers.html', context)

def addreview(request,id):
	user = User.objects.get(id=request.session['active_id'])
	book = Book.objects.get(id=id)
	review = request.POST['review']
	rating = request.POST['rating']

	Review.objects.create(rating=rating, content = review, user=user, book = book)
	
	return redirect('/books/{}'.format(book.id))
 
def delete(request,bookid,reviewid):
	review = Review.objects.get(id=reviewid)
	review.delete()
	return redirect('/books/{}'.format(bookid))

