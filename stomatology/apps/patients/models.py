from django.db import models
from django.contrib.auth.models import User

class Clients(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    date_birth = models.DateField()
