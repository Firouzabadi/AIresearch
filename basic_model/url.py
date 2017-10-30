from django.conf.urls import url

from . import views

urlpatterns = [
   url(r'^$', views.home, name='home'),
   url(r'^home/$', views.home, name='fa'),
   url(r'^mnist/$', views.mnist,name='mnist'),
   url(r'^setlabel/$', views.setlabel, name='setlabel'),
   url(r'^mnistregister/$', views.registerimage, name='registerimage'),
]