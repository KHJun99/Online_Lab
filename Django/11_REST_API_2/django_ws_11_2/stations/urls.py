from django.urls import path
from . import views

app_name = 'stations'

urlpatterns = [
    # Location
    path('locations/', views.location_list, name='location_list'),
    path('locations/<int:location_pk>/stations/', views.station_create, name='station_create'),
    
    # Station
    path('stations/', views.station_list, name='station_list'),
    path('stations/<int:station_pk>/', views.station_detail, name='station_detail'),
]