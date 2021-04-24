from django.urls import path
from . import views

urlpatterns = [
    path('', views.randomWord),
    path('random_word', views.randomWord)
]