from rest_framework import serializers
from .models import Location, Station


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'


class StationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = '__all__'
        read_only_fields = ('address',)


class StationListSerializer(serializers.ModelSerializer):
    """Station 목록 조회용 - address와 is_opening만"""
    class Meta:
        model = Station
        fields = ['id', 'address', 'is_opening']


class StationDetailSerializer(serializers.ModelSerializer):
    """Station 상세 조회용 - Location의 address 값을 포함한 모든 정보"""
    address = serializers.SerializerMethodField()
    
    class Meta:
        model = Station
        fields = ['id', 'address', 'total_ports', 'available_ports', 'is_opening']
    
    def get_address(self, obj):
        # address 필드를 중첩 객체로 반환
        return {'address': obj.address.address}