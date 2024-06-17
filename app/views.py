import imp
from django.shortcuts import render
from rest_framework import viewsets
from .serializer import *
from django.http import JsonResponse
import json

# Create your views here.
class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

class ScoreViewSet(viewsets.ModelViewSet):
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer

def process_json_data(request):
    if request.method == 'POST':
        try:
            #Jsonデータを取得
            json_data = json.loads(request.body.decode('utf-8'))

            #プレイヤー名の取得
            player_name_json = json_data.get('playerName')

            #プレイヤーがいるか確認していなければ新しく生成
            player_json, created = Player.objects.get_or_create(player_name=player_name_json)

            #スコアの取得
            score_json = json_data.get('score')

            #スコアの生成
            Score.objects.create(score=score_json, player_id=player_json)

            return JsonResponse({'message': 'Data processed successfully'}, status=200)
        
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid HTTP method'}, status=405)

def get_score_player_data(request):
    # スコアとプレイヤー名のデータを格納するリスト
    score_player_data = []

    # Scoreモデルの全てのインスタンスを取得
    all_scores = Score.objects.all()

    # 各スコアのインスタンスからスコアと関連するプレイヤー名を抽出し、リストに追加
    for score_instance in all_scores:
        score_player_data.append({
            'score': score_instance.score,
            'player_name': score_instance.player_id.player_name
        })

    # JsonResponseを使用してJSON形式でデータを返す
    return JsonResponse(score_player_data, safe=False)