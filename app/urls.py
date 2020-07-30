from django.urls import path        # django 2.0 doesn't support this
from django.contrib import admin
# from django.conf.urls import url
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('home', views.index, name='home'),
    path('suppliers', views.suppliers, name='suppliers'),
    path('my_product', views.my_product, name='my_product'),
    path('buyer', views.buyer, name='buyer'),
    path('login', views.login_view, name='login'),
]
