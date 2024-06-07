from django.db import models

# Create your models here.

class contact(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    phone = models.CharField(max_length=15)
    address = models.TextField()


