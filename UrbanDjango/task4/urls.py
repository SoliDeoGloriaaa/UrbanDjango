from django.urls import path

from task4 import views

app_name = 'task4'

urlpatterns = [
    path('main/', views.index, name='index'),
    path('shop/', views.shop, name='shop'),
    path('shop_cart/', views.shop_cart, name='shop_cart')
]
