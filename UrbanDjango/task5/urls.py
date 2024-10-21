from django.urls import path

from task5 import views

app_name = 'task5'

urlpatterns = [
    path('django/', views.sign_up_by_django, name='django'),
    path('html/', views.sign_up_by_html, name='html')
]