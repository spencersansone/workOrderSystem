from django.db import models

IMPORTANCE_CHOICES = (
    ("Urgent"),
    ("Normal"),
    ("Trivial"),
)

# class RequestEntry(models.Model):
#     title = models.CharField(max_length=100)
#     description = models.TextField(max_length=10000)
#     importance = models.CharField(max_length=100, choices=IMPORTANCE_CHOICES)
#     due_date = models.DateField()
    


# Create your models here.
