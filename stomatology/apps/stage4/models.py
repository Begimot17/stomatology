from django.db import models

from  card.models import Prosthesis

class Stages_4(models.Model):
    prosthesis = models.OneToOneField(Prosthesis, on_delete=models.CASCADE)
    quality_compatib = models.CharField(max_length=100)
    actions_perform = models.CharField(max_length=100)
    quality_instal = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    materials = models.CharField(max_length=100)
    conclusion = models.CharField(max_length=100)
    date_record = models.DateField(null=True)
    gate_check1 = models.DateField(null=True)
    gate_check2 = models.DateField(null=True)
    gate_check3 = models.DateField(null=True)
    gate_check4 = models.DateField(null=True)