from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Book, Review
from .serializers import (
    BookListSerializer, 
    BookSerializer,
    ReviewSerializer,
    ReviewListSerializer
)


@api_view(['GET', 'POST'])
def book_list(request):
    """
    GET: 모든 Book 조회 (title만)
    POST: 새로운 Book 생성
    """
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookListSerializer(books, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'DELETE'])
def book_detail(request, book_pk):
    """
    GET: 특정 Book 상세 조회
    DELETE: 특정 Book 삭제
    """
    book = get_object_or_404(Book, pk=book_pk)
    
    if request.method == 'GET':
        serializer = BookSerializer(book)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        isbn = book.isbn
        title = book.title
        book.delete()
        return Response(
            {'delete': f'도서 고유 번호 {isbn}번의 {title}을 삭제하였습니다.'},
            status=status.HTTP_204_NO_CONTENT
        )


@api_view(['POST'])
def review_create(request, book_pk):
    """
    특정 Book에 대한 Review 생성
    """
    book = get_object_or_404(Book, pk=book_pk)
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(book=book)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def review_list(request):
    """
    모든 Review 조회 (content와 score만)
    """
    reviews = Review.objects.all()
    serializer = ReviewListSerializer(reviews, many=True)
    return Response(serializer.data)