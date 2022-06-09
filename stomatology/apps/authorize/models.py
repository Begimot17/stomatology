from django.db import models
from django.contrib.auth.models import User


class Doctors(models.Model):
    def fio(self):
        return f'{self.user.last_name} {self.user.first_name}'
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    position = models.CharField(max_length=100)
