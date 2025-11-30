from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Todo
from .serializers import TodoSerializer, TodoListSerializer


@api_view(['GET', 'POST'])
def todo_list(request):
    """
    GET: 모든 Todo 조회
    POST: 새로운 Todo 생성
    """
    if request.method == 'GET':
        todos = Todo.objects.all()
        serializer = TodoListSerializer(todos, many=True)  # 여기 수정
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'DELETE'])
def todo_detail(request, todo_pk):
    """
    GET: 특정 Todo 상세 조회
    DELETE: 특정 Todo 삭제
    """
    todo = get_object_or_404(Todo, pk=todo_pk)
    
    if request.method == 'GET':
        serializer = TodoSerializer(todo)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)