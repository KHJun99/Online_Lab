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


class StationDetailSerializer(serializers.ModelSerializer):
    # address 필드를 address_id와 is_opening만 포함하도록 커스터마이징
    class Meta:
        model = Station
        fields = ['address', 'is_opening']