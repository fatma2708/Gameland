# game/views.py
from django.shortcuts import render
import random

colors = ['red', 'green', 'blue', 'yellow', 'pink', 'purple', 'orange', 'brown', 'black', 'white']

def color_game(request):
    if request.method == 'POST':
        user_guess = request.POST.get('color_guess').lower()
        correct_color = request.POST.get('correct_color').lower()
        if user_guess == correct_color:
            message = 'Correct! You guessed the right color!'
            message_color = 'green'
            game_over = True
        else:
            message = f'Incorrect. The correct color was {correct_color}. Try again!'
            message_color = 'red'
            game_over = True  # Set to True to end the game and display the message
    else:
        user_guess = ''
        correct_color = random.choice(colors)
        message = ''
        message_color = ''
        game_over = False

    context = {
        'correct_color': correct_color,
        'message': message,
        'message_color': message_color,
        'user_guess': user_guess,
        'game_over': game_over,
    }
    return render(request, 'colorguess/color_game.html', context)
