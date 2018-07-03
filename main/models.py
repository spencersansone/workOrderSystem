from django.db import models
from django.contrib.auth.models import User

IMPORTANCE_CHOICES = (
    ("E","1) Emergency"),
    ("S","2) Same Day"),
    ("N","3) Next Day"),
    ("B","4) By Appointment"),
)

class RequestEntry(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=10000)
    due_date = models.DateField()
    technician = models.ForeignKey(User, on_delete=models.CASCADE)
    


# Create your models here.
