from rest_framework import serializers
from .models import Todo, Recommend


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'


class TodoListSerializer(serializers.ModelSerializer):
    """Todo 목록 조회용 - work와 is_completed만"""
    class Meta:
        model = Todo
        fields = ['work', 'is_completed']


class RecommendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recommend
        fields = '__all__'
        read_only_fields = ('todo',)


class RecommendSerializerForTodoDetail(serializers.ModelSerializer):
    """Todo 상세 조회 시 Recommend 정보용 - id와 content만"""
    class Meta:
        model = Recommend
        fields = ['id', 'content']


class TodoDetailSerializer(serializers.ModelSerializer):
    """Todo 상세 조회용 - Recommend 포함"""
    recommend_set = RecommendSerializerForTodoDetail(many=True, read_only=True)
    
    class Meta:
        model = Todo
        fields = '__all__'