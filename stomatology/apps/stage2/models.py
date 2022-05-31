from django.db import models

from  card.models import Prosthesis

class Stages_2(models.Model):
    prosthesis = models.OneToOneField(Prosthesis, on_delete=models.CASCADE)
    dataX_ray = models.CharField(max_length=100)
    dataLab = models.CharField(max_length=100)
    dataAdd = models.CharField(max_length=100)
    conclusion = models.CharField(max_length=100)
    date_record = models.DateField(null=True)
    next_date = models.DateField(null=True)