from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Book
from .serializers import BookSerializer, BookDetailSerializer


# Create your views here.
@api_view(['GET'])
def book_list_or_create(request):
    if request.method == 'GET':
        book = Book.objects.all()
        serializer = BookSerializer(book, many=True)
        return Response(serializer.data)
    

@api_view(['GET'])
def book_detail(request, book_pk):
    if request.method == 'GET':
        book = Book.objects.get(pk=book_pk)
        serializer = BookDetailSerializer(book)
        return Response(serializer.data)