# number_guess/models.py

from django.db import models

class GameSession(models.Model):
    player_name = models.CharField(max_length=50)
    target_number = models.IntegerField()
    attempts = models.IntegerField(default=0)
    is_over = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
