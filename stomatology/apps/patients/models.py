from django.db import models
from django.contrib.auth.models import User

class Clients(models.Model):
    def fio(self):
        return f'{self.user.last_name} {self.user.first_name} {self.middle_name}'
    user= models.OneToOneField(User, on_delete=models.CASCADE)
    middle_name= models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    date_birth = models.DateField()
