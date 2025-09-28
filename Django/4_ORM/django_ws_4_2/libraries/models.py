from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.TextField(blank=True, default='')
    pubdate = models.DateField(null=True, blank=True)
    price = models.IntegerField(default=1)
    adult = models.BooleanField(default=False)