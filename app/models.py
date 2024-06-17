from operator import truediv
from tabnanny import verbose
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Player(models.Model):
    player_id = models.AutoField(primary_key=True)
    player_name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'player'
    def __str__(self):
        return self.player_name
    
class Score(models.Model):
    score_id = models.AutoField(primary_key=True)
    score = models.IntegerField()
    player_id = models.ForeignKey(Player, on_delete=models.CASCADE)
    add_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-score']
        verbose_name_plural = 'score'
    def __str__(self):
        return str(self.score)