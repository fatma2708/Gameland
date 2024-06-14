# number_guess/views.py

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import GameSession
import random

def home(request):
    return render(request, 'number_guess/homeG.html')

def start_game(request):
    if request.method == 'POST':
        player_name = request.POST.get('player_name')
        target_number = random.randint(1, 100)  # Change range as desired
        game_session = GameSession.objects.create(player_name=player_name, target_number=target_number)
        return redirect('play_game', game_id=game_session.id)
    return HttpResponse("Method not allowed")

def play_game(request, game_id):
    game_session = GameSession.objects.get(id=game_id)
    
    if request.method == 'POST':
        guess = int(request.POST.get('guess'))
        game_session.attempts += 1
        
        if guess == game_session.target_number:
            game_session.is_over = True
            game_session.save()
            return render(request, 'number_guess/win.html', {'game_session': game_session})
        else:
            if guess < game_session.target_number:
                feedback = "Try a higher number!"
            else:
                feedback = "Try a lower number!"
            return render(request, 'number_guess/play.html', {'game_session': game_session, 'feedback': feedback})
    
    return render(request, 'number_guess/play.html', {'game_session': game_session})
