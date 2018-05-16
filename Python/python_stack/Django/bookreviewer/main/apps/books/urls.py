from django.conf.urls import url, include
import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^books$', views.books),
    url(r'^logout$', views.logout),
    url(r'^books/add$', views.add),
    url(r'^addbook$', views.addbook),
    url(r'^books/(?P<id>\d+)$', views.showbook),

]