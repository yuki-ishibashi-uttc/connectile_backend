# config/urls.py

from django.contrib import admin
from django.urls import path, include  # ← include を追加！

urlpatterns = [
    path('admin/', admin.site.urls),

    # これが「プロジェクトの '大' 看板」です。
    # 「もしアクセスが来たら、'game' アプリの '専用看板（game/urls.py）' に
    # 案内を任せる」という設定です。
    path('', include('game.urls')),  # ← この行を追加！
]
