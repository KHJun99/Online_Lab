# Django Model

## 주요 개념

### 1. Model이란?
- **데이터베이스 스키마**: Python 클래스로 정의
- **ORM**: SQL 없이 DB 조작
- **필드**: 데이터 타입 정의
- **메소드**: 모델 동작 정의

### 2. 주요 필드 타입
- `CharField`: 문자열 (max_length 필수)
- `TextField`: 긴 텍스트
- `IntegerField`: 정수
- `BooleanField`: True/False
- `DateField`: 날짜
- `DateTimeField`: 날짜와 시간
- `ForeignKey`: 외래 키
- `ManyToManyField`: 다대다 관계

### 3. 마이그레이션
```bash
python manage.py makemigrations  # 마이그레이션 파일 생성
python manage.py migrate  # DB에 적용
```

## 예시 코드

### 기본 모델 정의
```python
# models.py
from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
```

### 외래 키 관계
```python
class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    published_date = models.DateField()

    def __str__(self):
        return self.title
```

## 기본 코드 템플릿

### 모델 기본 구조
```python
from django.db import models

class MyModel(models.Model):
    # 필드 정의
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_at']
        verbose_name = '모델명'
        verbose_name_plural = '모델명들'
```
