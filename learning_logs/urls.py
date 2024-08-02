"""Defines the URL patterns for  our app learning_logs"""

from django.urls import path

from . import views

app_name = 'learning_logs'

urlpatterns = [
    # Home  page

    path('', views.index, name='index'),

    # Topics page

    path('topics/', views.topics, name='topics'),

    # Detailed page for each topic 

    path('topics/<int:topic_id>/', views.topic, name='topic')
]
