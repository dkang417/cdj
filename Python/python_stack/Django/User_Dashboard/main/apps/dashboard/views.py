from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

# from .models import User

# Create your views here.
def index(request):
	# context = {
	# 	"users" : User.objects.all()
	# }	
	return render(request,'dashboard/index.html')
