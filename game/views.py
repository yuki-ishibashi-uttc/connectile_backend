# game/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import GameState
from .serializers import GameStateSerializer

class GameStateAPI(APIView):
    # この関数は、常に「ID=1」のゲームデータを
    # 取得するか、もし無ければ「作成」します。
    def get_object(self):
        # .get_or_create(id=1) は「id=1 を探す。無ければ作る」という魔法の命令
        obj, created = GameState.objects.get_or_create(id=1)
        return obj

    # GETリクエスト（データちょうだい）が来た時の処理
    def get(self, request):
        gamestate = self.get_object() # id=1 のデータを取得
        serializer = GameStateSerializer(gamestate) # データをJSONに翻訳
        return Response(serializer.data) # フロントエンドにJSONを返す

    # PUTリクエスト（データ上書きして）が来た時の処理
    def put(self, request):
        gamestate = self.get_object() # id=1 のデータを取得
        # フロントエンドから送られてきたJSON（request.data）で
        # gamestate のデータを上書きする
        serializer = GameStateSerializer(gamestate, data=request.data)
        if serializer.is_valid(): # データがルール通りかチェック
            serializer.save() # OKならセーブ
            return Response(serializer.data) # セーブ後のデータを返す
        return Response(serializer.errors, status=400) # ダメならエラーを返す