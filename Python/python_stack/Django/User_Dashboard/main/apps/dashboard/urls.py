
from django.conf.urls import url
from .import views

urlpatterns = [
	
    url(r'^$', views.index),
    url(r'^login$', views.login),
    url(r'^register$', views.register),
    url(r'^dashboard$', views.dashboard),
    # url(r'^users/create$', views.create),
    # url(r'^users/(?P<user_id>\d+)/delete$', views.delete),
    # url(r'^users/(?P<user_id>\d+)/edit$', views.edit),
    # url(r'^users/(?P<user_id>\d+)$', views.show_or_update)

]
