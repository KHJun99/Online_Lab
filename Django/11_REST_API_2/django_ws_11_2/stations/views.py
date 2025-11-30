from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Location, Station
from .serializers import (
    LocationSerializer, 
    StationSerializer,
    StationDetailSerializer
)


@api_view(['GET', 'POST'])
def location_list(request):
    """
    GET: location 정보 생성하는 기능
    POST: location 정보를 생성하는 기능
    """
    if request.method == 'GET':
        locations = Location.objects.all()
        serializer = LocationSerializer(locations, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = LocationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def station_create(request, location_pk):
    """
    station 정보 특정 조회하는 기능
    - station이 참조하는 location 정보는 사용자가 직접 입력하지 않음
    - address와 is_opening 정보를 제공
    """
    location = get_object_or_404(Location, pk=location_pk)
    serializer = StationSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(address=location)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def station_list(request):
    """
    station 상세 정보를 조회하는 기능
    - station의 모든 정보를 제공
    """
    stations = Station.objects.all()
    serializer = StationDetailSerializer(stations, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def station_detail(request, station_pk):
    """
    station 상세 정보 조회하는 기능
    - station의 모든 정보를 제공
    """
    station = get_object_or_404(Station, pk=station_pk)
    serializer = StationSerializer(station)
    return Response(serializer.data)