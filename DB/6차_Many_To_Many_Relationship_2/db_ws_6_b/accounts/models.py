from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    followings = models.ManyToManyField(
        'self',
        symmetrical=False,      # 대칭 관계 아님
        related_name='followers'    # 역참조 이름
    )
