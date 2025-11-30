from django.db import models

class Location(models.Model):
    address = models.CharField(max_length=100)
    
    def __str__(self):
        return self.address


class Station(models.Model):
    address = models.ForeignKey(Location, on_delete=models.CASCADE)
    total_ports = models.IntegerField()
    available_ports = models.IntegerField()
    is_opening = models.BooleanField()
    
    def __str__(self):
        return f"Station at {self.address.address}"


class Car(models.Model):
    station = models.ForeignKey(Station, on_delete=models.CASCADE)
    start_time = models.TimeField()
    model = models.CharField(max_length=100)
    is_payment = models.BooleanField()
    
    def __str__(self):
        return f"{self.model} at {self.station}"