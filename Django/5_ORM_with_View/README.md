# ORM with View

## 주요 개념

### 1. View에서 ORM 사용
- **데이터 조회**: DB에서 데이터 가져오기
- **템플릿 전달**: context로 데이터 전달
- **CRUD 구현**: Create, Read, Update, Delete

### 2. URL 패턴
```python
# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('articles/', views.article_list),
    path('articles/<int:pk>/', views.article_detail),
]
```

## 예시 코드

### 목록 조회
```python
# views.py
def article_list(request):
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'articles/list.html', context)
```

### 상세 조회
```python
def article_detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article
    }
    return render(request, 'articles/detail.html', context)
```

### 생성
```python
def article_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')

        article = Article.objects.create(
            title=title,
            content=content
        )
        return redirect('article_detail', article.pk)

    return render(request, 'articles/create.html')
```

## 기본 코드 템플릿

### CRUD Views
```python
from django.shortcuts import render, redirect

# 목록
def list_view(request):
    items = MyModel.objects.all()
    return render(request, 'list.html', {'items': items})

# 상세
def detail_view(request, pk):
    item = MyModel.objects.get(pk=pk)
    return render(request, 'detail.html', {'item': item})

# 생성
def create_view(request):
    if request.method == 'POST':
        MyModel.objects.create(
            field=request.POST.get('field')
        )
        return redirect('list')
    return render(request, 'create.html')

# 수정
def update_view(request, pk):
    item = MyModel.objects.get(pk=pk)
    if request.method == 'POST':
        item.field = request.POST.get('field')
        item.save()
        return redirect('detail', pk)
    return render(request, 'update.html', {'item': item})

# 삭제
def delete_view(request, pk):
    item = MyModel.objects.get(pk=pk)
    item.delete()
    return redirect('list')
```
