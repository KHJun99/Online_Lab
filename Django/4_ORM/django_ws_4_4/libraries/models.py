from django.db import models

# Create your models here.
class Libraries(models.Model):
    title = models.CharField(max_length=50)
    author = models.TextField()
    publisher = models.TextField()
    publishtime = models.DateField()
    salespoint = models.IntegerField()
    rating = models.FloatField()
    review = models.IntegerField()
    isbn = models.IntegerField()
    