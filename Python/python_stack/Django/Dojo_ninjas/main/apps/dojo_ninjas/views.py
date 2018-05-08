from django.shortcuts import render, HttpResponse, redirect
import random

def index(request):
	response = "heyyyyy coding ninjas"
	return HttpResponse(response)

