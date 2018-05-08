from django.shortcuts import render, HttpResponse, redirect
import random

def index(request):
	response = "heyyyyy user inputs"
	return HttpResponse(response)

