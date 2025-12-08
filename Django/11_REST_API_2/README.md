# Django REST API (2)

## 주요 개념

### 1. ViewSets
- **자동 CRUD**: 반복 코드 줄이기
- **Router**: URL 자동 생성

### 2. 인증과 권한
- **Authentication**: 사용자 확인
- **Permission**: 권한 확인
- **Token**: 토큰 기반 인증

### 3. 페이지네이션
- **PageNumberPagination**: 페이지 번호 방식
- **LimitOffsetPagination**: limit/offset 방식

## 예시 코드

### ViewSet 사용
```python
# views.py
from rest_framework import viewsets
from .models import Article
from .serializers import ArticleSerializer

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
```

### Router 설정
```python
# urls.py
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('articles', views.ArticleViewSet)

urlpatterns = router.urls
```

### 인증과 권한
```python
# settings.py
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ],
}

# views.py
from rest_framework.permissions import IsAuthenticated

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticated]
```

### 필터링과 검색
```python
from rest_framework import filters

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']
```

## 기본 코드 템플릿

### ViewSet 기본
```python
# views.py
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class MyViewSet(viewsets.ModelViewSet):
    queryset = MyModel.objects.all()
    serializer_class = MySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# urls.py
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('items', MyViewSet)
urlpatterns = router.urls
```
