from rest_framework import serializers
from .models import Book, Review


class BookListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('title',)


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('book',)


class ReviewListSerializer(serializers.ModelSerializer):
    """Review 목록 조회용 - content와 score만"""
    class Meta:
        model = Review
        fields = ['content', 'score']