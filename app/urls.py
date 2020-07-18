from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('home', views.index, name='home'),
    path('provider', views.provider, name='provider'),
    path('buyer', views.buyer, name='buyer'),
    path('login', views.login, name='login')
]
