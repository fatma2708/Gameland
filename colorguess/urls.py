# game/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.color_game, name='color_game'),
]
