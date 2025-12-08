# Many To Many Relationship (1) - M:N 관계

## 주요 개념

### 1. M:N 관계
- **다대다 관계**: 여러 레코드가 여러 레코드 참조
- **중개 테이블**: 관계를 저장하는 테이블
- **예시**: 학생-수업, 게시글-태그

### 2. Django에서 M:N
```python
class Student(models.Model):
    name = models.CharField(max_length=100)
    courses = models.ManyToManyField('Course')

class Course(models.Model):
    name = models.CharField(max_length=100)
```

### 3. ManyToManyField
- **자동 중개 테이블**: Django가 자동 생성
- **양방향 접근**: 양쪽에서 접근 가능

## 예시 코드

### M:N 모델 정의
```python
class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    tags = models.ManyToManyField(Tag, related_name='articles')

    def __str__(self):
        return self.title
```

### 관계 추가/제거
```python
# 게시글과 태그 생성
article = Article.objects.create(title='제목', content='내용')
tag1 = Tag.objects.create(name='Python')
tag2 = Tag.objects.create(name='Django')

# 태그 추가
article.tags.add(tag1)
article.tags.add(tag2)

# 태그 제거
article.tags.remove(tag1)

# 모든 태그 제거
article.tags.clear()
```

### 조회
```python
# 게시글의 모든 태그
article = Article.objects.get(id=1)
tags = article.tags.all()

# 태그의 모든 게시글
tag = Tag.objects.get(id=1)
articles = tag.articles.all()
```

## 기본 코드 템플릿

### M:N 모델
```python
class Item1(models.Model):
    name = models.CharField(max_length=100)
    items2 = models.ManyToManyField('Item2', related_name='items1')

class Item2(models.Model):
    name = models.CharField(max_length=100)
```
