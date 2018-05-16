from __future__ import unicode_literals
from django.db import models
from django import forms

from django.core.exceptions import ValidationError

# Create your models here.
class UserManager(models.Manager):
	def basic_validator(self,postData):
		errors={}
		#validate password		
		if len(postData['password']) < 8:
			errors["password"] = "password should be more than 8 characters"
		#checks that the passwords match
		if postData['password'] != postData['confirm']:
			errors["confirm"] = "passwords do not match"
		return errors

class User(models.Model):
	name = models.CharField(max_length=255)
	alias = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	password = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	objects = UserManager()



class AuthorManager(models.Manager):
	def validate_author(request, postData):
		errors = {}
		return errors
class Author(models.Model):
	author = models.CharField(max_length=255)
	objects = AuthorManager()



class BookManager(models.Manager):
	def validate_book(request,postData):
		errors = {}
		return errors
class Book(models.Model):
	title = models.CharField(max_length=255)
	author = models.ForeignKey(Author, related_name="books")
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	objects = BookManager()


class ReviewManager(models.Manager):
	def validate_review(request, postData):
		errors = {}
		return errors
class Review(models.Model):
	rating = models.IntegerField()
	comment = models.TextField()
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	book = models.ForeignKey(Book, related_name="reviews")
	user = models.ForeignKey(User, related_name="reviews")
	objects = ReviewManager()

