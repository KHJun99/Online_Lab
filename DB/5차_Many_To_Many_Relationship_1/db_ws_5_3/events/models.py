from django.db import models

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    location = models.TextField()
    participant = models.ManyToManyField('Participant', related_name='events')


class Participant(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    registration_date = models.DateField(auto_now_add=True)