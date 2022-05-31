from django.db import models
from patients.models import Clients
from materials.models import *



class PatientCard(models.Model):
    client = models.OneToOneField(Clients, on_delete=models.CASCADE)
    status = models.CharField(max_length=100)


class Prosthesis(models.Model):
    card = models.OneToOneField(PatientCard, on_delete=models.CASCADE)
    type = models.ForeignKey(Type_prost, on_delete=models.CASCADE, null=True)
    construction = models.ForeignKey(Construction, on_delete=models.CASCADE, null=True)
    material = models.ForeignKey(Materials, on_delete=models.CASCADE, null=True)
