from django.urls import path, include
from django.contrib import admin
from . import views


urlpatterns = [
    path('', views.user_dispather, name='home'),
    path('home', views.user_dispather, name='home'),
    path('suppliers', views.suppliers, name='suppliers'),
    path('my_product', views.my_product, name='my_product'),
    path('buyer', views.buyer, name='buyer'),
    path('accounts/', include('django.contrib.auth.urls')),
]

admin.site.site_header = "Bivni Mamonta Admin"
admin.site.site_title = "Bivni Mamonta Bazar"
admin.site.index_title = "Welcome site manager"