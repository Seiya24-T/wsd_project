from unicodedata import name
from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('add_youtube/<int:id>', views.add_youtube, name='add_youtube'),
    path('detail/<int:id>/', views.detail, name='detail'),
    path('add_person/', views.add_person, name='add_person'),
    path('add_artist/', views.add_artist, name=('add_artist')),
]
