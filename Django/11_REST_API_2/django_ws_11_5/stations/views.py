from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Location, Station, Car
from .serializers import (
    LocationSerializer, 
    StationSerializer,
    StationListSerializer,
    StationDetailSerializer,
    CarSerializer,
    CarDetailSerializer
)


@api_view(['GET', 'POST'])
def location_list(request):
    """
    GET: location 정보 조회하는 기능
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
    station 정보 생성하는 기능
    - station이 참조하는 location 정보는 사용자가 직접 입력하지 않음
    """
    location = get_object_or_404(Location, pk=location_pk)
    serializer = StationSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(address=location)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def station_list(request):
    """
    station 목록 조회하는 기능
    - address와 is_opening만 반환
    """
    stations = Station.objects.all()
    serializer = StationListSerializer(stations, many=True)
    return Response(serializer.data)


@api_view(['GET', 'DELETE'])
def station_detail(request, station_pk):
    """
    GET: station 상세 정보 조회하는 기능
    DELETE: station 삭제하는 기능
    """
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


@api_view(['POST'])
def car_create(request, station_pk):
    """
    car 생성 기능을 구현
    - car가 참조하는 stations 정보는 사용자가 직접 입력하지 않음
    """
    station = get_object_or_404(Station, pk=station_pk)
    serializer = CarSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(station=station)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT'])
def car_detail(request, car_pk):
    """
    GET: car 상세 정보를 확인 및 수정 가능 기능을 구현
    PUT: car 가격 모든 정보를 제공
    - 수정 가능 정보는 is_payment만 수정할 수 있다
    - 수정이 완료되면 car의 전체 정보를 반환한다
    """
    car = get_object_or_404(Car, pk=car_pk)
    
    if request.method == 'GET':
        serializer = CarDetailSerializer(car)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = CarSerializer(car, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)