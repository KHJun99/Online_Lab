from django.db import models
from django.conf import settings

# Create your models here.
class Diary(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='diaries')
    content = models.CharField(max_length=125)
    picture = models.ImageField(blank=True, upload_to='diary/%y/%b/%a')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='liked_diaries', blank=True)

    def __str__(self):
        return f'{self.user.username}의 일기 - {self.created_at.strftime("%Y.%m.%d")}'

class Comment(models.Model):
    diary = models.ForeignKey(Diary, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=125)
    created_at = models.DateTimeField(auto_now_add=True)