from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu, name='menu'),        # intro page
    path('game/', views.game, name='game'),   # game page
    path('', views.player, name='player'),
]
