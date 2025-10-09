from django.urls import path
from . import views

app_name = 'memos'
urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),           # 작성 페이지(GET)
    path('create/', views.create, name='create'),  # 생성 처리(POST)
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/delete/', views.delete, name='delete'),
]
