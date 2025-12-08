# Many To One Relationship (2) - N:1 심화

## 주요 개념

### 1. related_name
- **역참조 이름**: 부모에서 자식 접근 시 사용
- **기본값**: `모델명_set`
- **커스텀**: `related_name='custom_name'`

### 2. 댓글 기능 구현
- **게시글-댓글**: 전형적인 N:1 관계
- **역참조**: 게시글의 모든 댓글 조회

## 예시 코드

### 댓글 모델
```python
class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content[:20]
```

### 댓글 CRUD
```python
# 댓글 생성
article = Article.objects.get(id=1)
comment = Comment.objects.create(
    article=article,
    content='댓글 내용'
)

# 댓글 조회
article = Article.objects.get(id=1)
comments = article.comments.all()

# 댓글 개수
comment_count = article.comments.count()
```

### View에서 사용
```python
def article_detail(request, pk):
    article = Article.objects.get(pk=pk)
    comments = article.comments.all()

    context = {
        'article': article,
        'comments': comments,
    }
    return render(request, 'detail.html', context)
```

## 기본 코드 템플릿

### 댓글 시스템
```python
# models.py
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
```
