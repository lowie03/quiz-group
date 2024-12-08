from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('game', views.game, name='game'),
    path('end/', views.end, name='end'),
    path('highscores', views.highscores, name='highscores'),
    path('register', views.registerPage, name = "register"),
    path('login', views.loginPage, name = "login"),
    path('logout', views.logoutUser, name = "logout")
]