from __future__ import unicode_literals
from django.db import models
from django import forms

from django.core.validators import validate_email
from django.core.exceptions import ValidationError

# Create your models here.
class UserManager(models.Manager):
	def basic_validator(self,postData):
		errors={}
		
		if len(postData['first_name']) < 2:
			errors["first_name"] = "first name should be more than 2 characters"

		if len(postData['last_name']) < 2:
			errors["last_name"] = "last name should be more than 2 characters"
		
		#validate email 
		try:
			validate_email(postData['email'])
		except ValidationError:
			errors['email'] = "this is not a valid email"
		else: 
			if User.objects.filter(email=postData['email']):
				errors['Email'] = "this user already exists"

		#validate password		
		if len(postData['password']) < 8:
			errors["password"] = "password should be more than 8 characters"

		if postData['password'] != postData['confirm']:
			errors["confirm"] = "passwords do not match"
		return errors

class User(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email=models.CharField(max_length=255)
	password=models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	
	objects = UserManager()
	
