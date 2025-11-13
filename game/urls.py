# game/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # もし 'api/gamestate/' という住所（URL）でアクセスが来たら、
    # views.py の GameStateListCreate シェフ（クラス）に繋ぐ、という意味です。
    path('api/gamestate/', views.GameStateAPI.as_view(), name='gamestate-list-create'),
]
