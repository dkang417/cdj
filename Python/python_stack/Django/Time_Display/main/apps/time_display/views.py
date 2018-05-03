from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime


def index(request):
	context = {
	"date":strftime("%Y-%m-%d"),
	"time":strftime("%H:%M %p")
	}
	return render(request,'time_display/index.html',context)