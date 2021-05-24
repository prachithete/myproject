from django.urls import path

from . import views 

app_name = "tasks"  #This will help to uniquely identify urls 
urlspattern[
    path("", views.index, name="index"),
    path("add", views.add, name="add")
]