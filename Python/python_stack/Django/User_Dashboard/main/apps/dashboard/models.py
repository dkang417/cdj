from __future__ import unicode_literals

from django.db import models

# Create your models here.
class UserManager(models.Manager):
	def basic_validator(self,postData):
		errors={}
		#validate password		
		if len(postData['password']) < 8:
			errors["password"] = "password should be more than 8 characters"

		if postData['password'] != postData['confirm']:
			errors["confirm"] = "passwords do not match"
		return errors

class User(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email= models.CharField(max_length=255)
	password=models.CharField(max_length=255)
	# user_level = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	objects = UserManager()

class Message(models.Model):
	comment = models.TextField(max_length = 1000)
	desc = models.TextField(max_length = 1000)
	created_at= models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now=True)
	user = models.ForeignKey(User, related_name = "messages")

class Description(models.Model):
	comment=  models.TextField(max_length = 1000)
	created_at= models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now=True)
	user = models.ForeignKey(User, related_name = "descriptions")

