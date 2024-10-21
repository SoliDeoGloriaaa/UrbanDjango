from django.contrib import admin
from django.urls import path, include
from task2 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index_for_func),
    path('class/', views.IndexForClass.as_view()),
    path('task3/', include('task3.urls', namespace='task3')),
    path('task4/', include('task4.urls', namespace='task4')),
    path('task5/', include('task5.urls', namespace='task5'))
]
