from unicodedata import name
from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('add_youtube/', views.add_youtube, name='add_youtube'),
    path('detail/<int:pk>/', views.detail, name='detail'),
]
