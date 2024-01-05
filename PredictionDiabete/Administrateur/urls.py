from django.conf.urls import include
from django.conf.urls.static import static
from django.conf import settings
from django.urls import include, path, re_path

from Administrateur import views

urlpatterns=[
    re_path(r'^$', views.login, name='login'), 
    re_path(r'^login', views.login, name='login'),
    re_path(r'^accueil', views.accueil, name='accueil'),
    re_path(r'^prediction', views.prediction, name='prediction'),
]