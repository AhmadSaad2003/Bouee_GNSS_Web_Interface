from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('logout/', views.logoutuser, name="logout"),

    path('home/', views.home, name="home"),
    path('affiche/', views.affiche, name="affiche"),
    path('affichetemp/', views.affichetemp, name="affichetemp"),
    path('affichepress/', views.affichepress, name="affichepress"),
    path('affichehum/', views.affichehum, name="affichehum"),
    path('affichemap/', views.affichemap, name="affichemap"),
]   
