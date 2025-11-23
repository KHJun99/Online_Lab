from django.urls import path
from . import views


app_name = 'libraries'

urlpatterns = [
    path('', views.index, name='index'),  # 메인 페이지 추가
    path('create_author/', views.create_author, name='create_author'),
    path('books/', views.books, name='books'),
    path('books/create/', views.books_create, name='books_create'),
    path('authors/<int:author_pk>/', views.author_detail, name='author_detail'),  # 작가 프로필
    path('authors/<int:author_pk>/subscribe/', views.author_subscribe, name='author_subscribe'),  # 구독 기능
]