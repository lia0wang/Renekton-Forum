"""Defines URL patterns or this app"""
from django.urls import path # when mapping urls to views
from . import views

app_name = 'app_renekton'
# list of urls that can be requested from the current app
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    path('topics/', views.topics, name='topics'),
    path('topics/<int:topic_id>/', views.topic, name='topic'),
]

