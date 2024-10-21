from django.urls import path

from task3 import views

app_name = 'task3'

urlpatterns = [
    path('main/', views.index, name='index'),
    path('shop/', views.shop, name='shop'),
    path('shop_cart/', views.shop_cart, name='shop_cart')
]
