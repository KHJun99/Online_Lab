# Many To One Relationship (1) - N:1 관계

## 주요 개념

### 1. N:1 관계
- **다대일 관계**: 여러 레코드가 하나의 레코드 참조
- **외래 키(Foreign Key)**: 다른 테이블의 기본 키 참조
- **예시**: 여러 게시글(N) - 하나의 작성자(1)

### 2. Django에서 N:1
```python
class Author(models.Model):
    name = models.CharField(max_length=100)

class Article(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
```

### 3. on_delete 옵션
- **CASCADE**: 참조 객체 삭제 시 함께 삭제
- **PROTECT**: 참조 객체 삭제 방지
- **SET_NULL**: NULL로 설정
- **SET_DEFAULT**: 기본값으로 설정

## 예시 코드

### 모델 정의
```python
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    published_date = models.DateField()

    def __str__(self):
        return self.title
```

### 데이터 생성
```python
# 작성자 생성
author = Author.objects.create(name='홍길동', email='hong@example.com')

# 책 생성
book = Book.objects.create(
    title='Django 입문',
    author=author,
    published_date='2024-01-01'
)
```

### 역참조
```python
# 정참조: 책 → 작성자
book = Book.objects.get(id=1)
print(book.author.name)

# 역참조: 작성자 → 책들
author = Author.objects.get(id=1)
books = author.books.all()
for book in books:
    print(book.title)
```

## 기본 코드 템플릿

### N:1 모델
```python
class Parent(models.Model):
    name = models.CharField(max_length=100)

class Child(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey(
        Parent,
        on_delete=models.CASCADE,
        related_name='children'
    )
```
