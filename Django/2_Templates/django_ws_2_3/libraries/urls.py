from django.urls import path, include
from libraries import views

urlpatterns = [
    path('', views.index),
    path('recommend/', views.recommend, name='recommend'),
]