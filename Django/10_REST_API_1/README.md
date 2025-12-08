# Django REST API (1)

## 주요 개념

### 1. REST API
- **RESTful**: 자원 기반 아키텍처
- **HTTP 메소드**: GET, POST, PUT, DELETE
- **JSON**: 데이터 포맷
- **Endpoint**: API URL

### 2. Django REST Framework (DRF)
```bash
pip install djangorestframework
```

### 3. Serializer
- **데이터 직렬화**: 모델 → JSON
- **역직렬화**: JSON → 모델

## 예시 코드

### Serializer 정의
```python
# serializers.py
from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
```

### API View
```python
# views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Article
from .serializers import ArticleSerializer

@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET', 'PUT', 'DELETE'])
def article_detail(request, pk):
    article = Article.objects.get(pk=pk)

    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        article.delete()
        return Response(status=204)
```

### URL 설정
```python
# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('api/articles/', views.article_list),
    path('api/articles/<int:pk>/', views.article_detail),
]
```

## 기본 코드 템플릿

### DRF 기본 설정
```python
# settings.py
INSTALLED_APPS = [
    ...
    'rest_framework',
]

# serializers.py
from rest_framework import serializers

class MySerializer(serializers.ModelSerializer):
    class Meta:
        model = MyModel
        fields = '__all__'

# views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET', 'POST'])
def api_list(request):
    if request.method == 'GET':
        items = MyModel.objects.all()
        serializer = MySerializer(items, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
```
