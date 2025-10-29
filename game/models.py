# game/models.py

from django.db import models

# 私たちの『Connectile』のゲーム状態を丸ごと保存する
# 「棚（テーブル）」の設計図です。
class GameState(models.Model):
    
    # プレイヤー1の所持ポイントを保存する「引き出し（カラム）」
    # IntegerField = 整数（数字）だけを保存できる。
    # default=0 = もし何も指定されなければ、自動で 0 を入れておく。
    player1_points = models.IntegerField(default=0)
    player2_points = models.IntegerField(default=0)
    player3_points = models.IntegerField(default=0)
    player4_points = models.IntegerField(default=0)
    
    # 盤面の状態（[ [0,0,..], [0,1,..], ...]）を保存する「引き出し」
    # JSONField = Pythonのリスト（配列）や辞書（オブジェクト）を
    # そのままの形で保存できる、非常に便利な引き出し。
    # default=list は、「もし何も指定されなければ、空のリスト[]を入れておく」という指定です。
    board_state = models.JSONField(default=list) 

    # これは管理画面などで見やすくするための、おまじないです
    def __str__(self):
        # f"..." はPythonのフォーマット済み文字列です
        return f"Game State (ID: {self.id})"