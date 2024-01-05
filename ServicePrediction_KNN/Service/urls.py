#-*- coding: utf-8 -*-
from django.conf.urls.static import static
from django.urls import include, path, re_path
from Service import views
urlpatterns=[ 
    re_path(r'^prediction/(?P<highBP>[\w\W])/(?P<highChol>[\w\W]+)/(?P<cholCheck>[\w\W]+)/(?P<bMI>[\w\W]+)/(?P<smoker>[\w\W]+)/(?P<stroke>[\w\W]+)/(?P<heartDiseaseorAttack>[\w\W]+)/(?P<physActivity>[\w\W]+)/(?P<fruits>[\w\W]+)/(?P<veggies>[\w\W]+)/(?P<sex>[\w\W]+)/(?P<age>[\w\W]+)$', views.prediction, name='prediction'),
    re_path(r'^creation_model/(?P<highBP>[\w\W])/(?P<highChol>[\w\W]+)/(?P<cholCheck>[\w\W]+)/(?P<bMI>[\w\W]+)/(?P<smoker>[\w\W]+)/(?P<stroke>[\w\W]+)/(?P<heartDiseaseorAttack>[\w\W]+)/(?P<physActivity>[\w\W]+)/(?P<fruits>[\w\W]+)/(?P<veggies>[\w\W]+)/(?P<sex>[\w\W]+)/(?P<age>[\w\W]+)$', views.creation_model, name='creation_model'),
]