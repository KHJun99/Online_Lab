from django.urls import path
from . import views

app_name = 'libraries'

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.books, name='books'),
    path('books/create/', views.create_book, name='create_book'),
    path('accounts/profile/<str:username>/', views.profile, name='profile'),  # URL 수정
    path('authors/create/', views.create_author, name='create_author'),
]