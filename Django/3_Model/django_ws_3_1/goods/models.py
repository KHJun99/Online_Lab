from django.db import models

# Create your models here.
class Goods(models.Model):
    name = models.TextField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    is_published = models.BooleanField()
