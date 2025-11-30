from rest_framework import serializers
from .models import Location, Station, Car


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'
        
        
class StationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = '__all__'
        

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'
        read_only_fields = ('station',)


class StationDetailSerializer(serializers.ModelSerializer):
    car_set = CarSerializer(many=True, read_only=True)
    
    class Meta:
        model = Station
        fields = '__all__'
        

class CarDetailSerializer(serializers.ModelSerializer):
    station = StationSerializer(read_only=True)
    
    class Meta:
        model = Car
        fields = '__all__'