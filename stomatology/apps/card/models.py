from django.db import models
from patients.models import Clients



class PatientCard(models.Model):
    client = models.ForeignKey(Clients, on_delete=models.CASCADE)
    status = models.CharField(max_length=100)


class Prosthesis(models.Model):
    card = models.ForeignKey(PatientCard, on_delete=models.CASCADE)
    type = models.CharField(max_length=100)
    construction = models.CharField(max_length=100)
