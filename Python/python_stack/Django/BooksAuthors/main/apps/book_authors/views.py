from django.shortcuts import render, HttpResponse, redirect
import random

def index(request):
	response = "heyyyyy books and authors!!!!"
	return HttpResponse(response)

