# Django ORM

## 주요 개념

### 1. ORM이란?
- **Object-Relational Mapping**: 객체와 DB 테이블 매핑
- **QuerySet**: 데이터 조회 결과
- **CRUD**: Create, Read, Update, Delete

### 2. 주요 메소드
- `all()`: 모든 데이터
- `get()`: 단일 데이터
- `filter()`: 조건 필터링
- `exclude()`: 제외
- `order_by()`: 정렬
- `create()`: 생성
- `save()`: 저장
- `delete()`: 삭제

## 예시 코드

### CRUD 작업
```python
# Create
article = Article.objects.create(
    title='제목',
    content='내용'
)

# Read
articles = Article.objects.all()
article = Article.objects.get(id=1)
filtered = Article.objects.filter(title__contains='Django')

# Update
article.title = '새 제목'
article.save()

# Delete
article.delete()
```

### 조회 필터링
```python
# 필터 조건
Article.objects.filter(title__contains='Django')
Article.objects.filter(created_at__year=2024)
Article.objects.filter(is_published=True)
Article.objects.exclude(title='Test')

# 정렬
Article.objects.order_by('-created_at')
Article.objects.order_by('title')

# 개수 제한
Article.objects.all()[:5]  # 처음 5개
```

## 기본 코드 템플릿

### QuerySet 기본
```python
# 전체 조회
all_items = MyModel.objects.all()

# 필터링
filtered = MyModel.objects.filter(field=value)

# 단일 조회
item = MyModel.objects.get(id=1)

# 생성
new_item = MyModel.objects.create(field=value)

# 수정
item.field = new_value
item.save()

# 삭제
item.delete()
```
