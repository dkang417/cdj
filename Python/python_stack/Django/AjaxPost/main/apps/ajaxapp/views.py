from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from models import *
from django.core import serializers
import json

def index(request):
	return render(request,"ajaxapp/index.html")

def add(request):
	note = request.POST['note']
	post = "<div class='post'>{}</div>".format(note)
	return HttpResponse(post)