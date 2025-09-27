from django.urls import path
from my_app import views

app_name = 'introduce'
urlpatterns = [
    path('<str:username>', views.introduce, name='introduce')
    
]
