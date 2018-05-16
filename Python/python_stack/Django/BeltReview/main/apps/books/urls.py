from django.conf.urls import url
from .import views

urlpatterns = [
	
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^books$', views.books),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^books/add$', views.booksadd),
    url(r'^processreview$', views.add),
    url(r'^books/(?P<id>\d+)$' ,views.bookpage)
]
