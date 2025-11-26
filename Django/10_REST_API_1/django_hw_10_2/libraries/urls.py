from django.urls import path
from . import views


urlpatterns = [
    path('libraries/', views.book_list_or_create),
    path('libraries/<int:book_pk>/', views.book_detail)
    
]
