# game/models.py

from django.db import models

# 8x8の「空の盤面」データを作るための関数
def get_default_board():
    # [0,0,0,0,0,0,0,0] というリストを8個作る
    return [[0 for _ in range(8)] for _ in range(8)]

class GameState(models.Model):
    player1_points = models.FloatField(default=0.0) # ← IntegerField を FloatField に変更
    player2_points = models.FloatField(default=0.0) # ← IntegerField を FloatField に変更
    player3_points = models.FloatField(default=0.0) # ← IntegerField を FloatField に変更
    player4_points = models.FloatField(default=0.0) # ← IntegerField を FloatField に変更
    board_state = models.JSONField(default=list)

    def __str__(self):
        return f"Game State (ID: {self.id})"