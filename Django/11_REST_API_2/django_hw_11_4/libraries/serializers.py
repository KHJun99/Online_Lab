from rest_framework import serializers
from .models import Book, Review


class BookListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('title',)


class ReviewForBookDetailSerializer(serializers.ModelSerializer):
    """도서 상세 조회 시 리뷰 정보용 - content와 score만"""
    class Meta:
        model = Review
        fields = ('content', 'score')


class BookSerializer(serializers.ModelSerializer):
    """도서 상세 조회용 - 리뷰 목록 포함"""
    review_set = ReviewForBookDetailSerializer(many=True, read_only=True)
    review_count = serializers.IntegerField(source='review_set.count', read_only=True)
    
    class Meta:
        model = Book
        fields = '__all__'


class BookForReviewSerializer(serializers.ModelSerializer):
    """리뷰 조회 시 도서 정보용 - isbn만"""
    class Meta:
        model = Book
        fields = ('isbn',)


class ReviewListSerializer(serializers.ModelSerializer):
    """리뷰 목록 조회용 - 도서의 isbn 포함"""
    book = BookForReviewSerializer(read_only=True)
    
    class Meta:
        model = Review
        fields = ('book', 'content', 'score')


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('book',)