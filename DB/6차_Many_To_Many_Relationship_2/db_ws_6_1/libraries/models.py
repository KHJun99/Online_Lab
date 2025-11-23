from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Author(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=20)
    # User와 M:N 관계 (중개 테이블: author_subscribed_users)
    subscribed_users = models.ManyToManyField(
        User,
        related_name='subscribed_authors',
        through='AuthorSubscription'
    )
    
    def __str__(self):
        return self.nickname


class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    title = models.CharField(max_length=100)
    description = models.TextField()
    genre = models.TextField()
    
    def __str__(self):
        return self.title


# 중개 모델 (Author와 User 사이)
class AuthorSubscription(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'author_subscribed_users'  # 중개 테이블 이름 지정
        unique_together = ('author', 'user')
    
    def __str__(self):
        return f'{self.user.username} - {self.author.nickname}'