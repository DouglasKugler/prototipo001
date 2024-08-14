
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    
    path('register', views.register, name='register'),
    #path('logout', views.logout, name='logout'), 
    path('principal', views.principal, name='principal'),
    path('profile', views.profile, name='profile'),
    #path('login', views.login, name='login'), 
    path('proposta', views.proposta, name='proposta'),
    
]