# game/serializers.py

from rest_framework import serializers
from .models import GameState

# GameStateの「棚」を「JSON」に翻訳するルールブック
class GameStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameState  # 翻訳する「棚（モデル）」はGameStateです
        # 翻訳の対象にする「引き出し（フィールド）」を指定
        fields = ['id', 'player1_points', 'player2_points', 'player3_points', 'player4_points', 'board_state']