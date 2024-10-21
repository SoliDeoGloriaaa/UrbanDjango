from django.contrib import admin
from django.urls import path
from task2 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index_for_func),
    path('class/', views.IndexForClass.as_view())
]
