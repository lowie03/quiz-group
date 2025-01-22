<<<<<<< HEAD
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
=======
# from django.urls import path

# from . import views

# urlpatterns = [
#     path("", views.index, name="index"),
#     path('game', views.game, name='game'),
#     # path('end/', views.end, name='end'),
#     # path('highscores', views.highscores, name='highscores'),
#     # path('register', views.registerPage, name = "register"),
#     # path('login', views.loginPage, name = "login"),
#     # path('logout', views.logoutUser, name = "logout")
# ]

# from django.urls import path
# from .views import IndexView, GameView, EndView, HighscoresView, RegisterView, LoginView, LogoutView

# urlpatterns = [
#     path('', IndexView.as_view(), name='index'),
#     path('game', GameView.as_view(), name='game'),
#     path('end', EndView.as_view(), name='end'),
#     path('highscores', HighscoresView.as_view(), name='highscores'),
#     path('register', RegisterView.as_view(), name='register'),
#     path('login', LoginView.as_view(), name='login'),
#     path('logout', LogoutView.as_view(), name='logout'),
# ]



from django.urls import path
from .views import IndexView, GameView, EndView, HighscoresView, RegisterView, LoginView, LogoutView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('game', GameView.as_view(), name='game'),
    path('end', EndView.as_view(), name='end'),
    path('highscores', HighscoresView.as_view(), name='highscores'),
    path('register', RegisterView.as_view(), name='register'),
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
>>>>>>> b1fe81c (updates)
]