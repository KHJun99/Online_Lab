from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Location, Station
from .serializers import (
    LocationSerializer, 
    StationSerializer,
    StationListSerializer,
    StationDetailSerializer
)


@api_view(['GET', 'POST'])
def location_list(request):
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
    location = get_object_or_404(Location, pk=location_pk)
    serializer = StationSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(address=location)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def station_list(request):
    stations = Station.objects.all()
    serializer = StationListSerializer(stations, many=True)
    return Response(serializer.data)


@api_view(['GET', 'DELETE'])
def station_detail(request, station_pk):
    station = get_object_or_404(Station, pk=station_pk)
    
    if request.method == 'GET':
        serializer = StationDetailSerializer(station)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        address_name = station.address.address
        station_id = station.pk
        station.delete()
        return Response(
            {'delete': f'{address_name}의 등록 번호 \'{station_id}\'번 충전소 정보가 삭제되었습니다.'},
            status=status.HTTP_204_NO_CONTENT
        )