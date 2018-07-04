from django.db import models
from django.contrib.auth.models import User

LOCATION_CHOICES = (
    ("B1","Building 1"),
    ("B2","Building 2"),
    ("B3","Building 3"),
    ("B4","Building 4"),
)

class Client(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100,choices=LOCATION_CHOICES)
    room_number = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    
    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

class CommonArea(models.Model):
    area_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100,choices=LOCATION_CHOICES)
    
    def __str__(self):
        return "{}".format(self.area_name)

class ClientRequest(models.Model):
    title = models.CharField(max_length=100)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    description = models.TextField(max_length=10000)
    due_date = models.DateField()
    technician = models.ForeignKey(User, on_delete=models.CASCADE)

class CommonAreaRequest(models.Model):
    title = models.CharField(max_length=100)
    common_area = models.ForeignKey(CommonArea, on_delete=models.CASCADE)
    description = models.TextField(max_length=10000)
    due_date = models.DateField()
    technician = models.ForeignKey(User, on_delete=models.CASCADE)