# number_guess/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='homet'),
    path('start/', views.start_game, name='start_game'),
    path('play/<int:game_id>/', views.play_game, name='play_game'),
]
