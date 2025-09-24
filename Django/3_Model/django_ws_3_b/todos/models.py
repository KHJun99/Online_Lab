from django.db import models

# Create your models here.
class Todo(models.Model):
    group = models.TextField()
    user = models.TextField()