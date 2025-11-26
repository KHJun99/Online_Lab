from rest_framework import serializers
from .models import Artist


# 전체 목록 조회용 (이름, 데뷔일만)
class ArtistListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ('name', 'debut_date')


# 상세 정보 조회용 (모든 정보)
class ArtistSerializer(serializers.ModelSerializer):

    class Meta:
        model = Artist
        fields = '__all__'