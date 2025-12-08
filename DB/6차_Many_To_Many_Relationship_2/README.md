# Many To Many Relationship (2) - M:N 심화

## 주요 개념

### 1. 좋아요 기능
- **User-Article**: M:N 관계
- **자기 자신 참조**: User-User (팔로우)

### 2. through 모델
- **중개 모델 커스터마이징**: 추가 필드 정의
- **through_fields**: 필드 명시

## 예시 코드

### 좋아요 기능
```python
from django.contrib.auth.models import User

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(
        User,
        related_name='like_articles',
        blank=True
    )
```

### 좋아요 추가/제거
```python
# View
def like_article(request, pk):
    article = Article.objects.get(pk=pk)
    user = request.user

    # 이미 좋아요했는지 확인
    if article.like_users.filter(pk=user.pk).exists():
        # 좋아요 취소
        article.like_users.remove(user)
    else:
        # 좋아요 추가
        article.like_users.add(user)

    return redirect('article_detail', pk)
```

### 팔로우 기능
```python
class User(AbstractUser):
    followings = models.ManyToManyField(
        'self',
        symmetrical=False,
        related_name='followers'
    )
```

### through 모델
```python
class Person(models.Model):
    name = models.CharField(max_length=100)

class Group(models.Model):
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(
        Person,
        through='Membership'
    )

class Membership(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined = models.DateField()
    role = models.CharField(max_length=50)
```

## 기본 코드 템플릿

### 좋아요 시스템
```python
# models.py
from django.contrib.auth.models import User

class Post(models.Model):
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(
        User,
        related_name='like_posts',
        blank=True
    )

# views.py
def toggle_like(request, pk):
    post = Post.objects.get(pk=pk)

    if post.like_users.filter(pk=request.user.pk).exists():
        post.like_users.remove(request.user)
        liked = False
    else:
        post.like_users.add(request.user)
        liked = True

    return JsonResponse({
        'liked': liked,
        'count': post.like_users.count()
    })
```
