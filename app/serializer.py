from dataclasses import fields
from rest_framework import serializers
from .models import *

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = [
            'player_id',
            'player_name',
        ]

class ScoreSerializer(serializers.ModelSerializer):
    #player_name = serializers.CharField(source='Player.player_name', read_only=True)
    
    class Meta:
        model = Score
        fields = [
            'score_id',
            'score',
            'player_id',
            #'player_name',
            'add_date',
        ]