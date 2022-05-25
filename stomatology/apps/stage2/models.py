from django.db import models

from  card.models import Prosthesis

class Stages_2(models.Model):
    prosthesis = models.ForeignKey(Prosthesis, on_delete=models.CASCADE)
    dataX_ray = models.CharField(max_length=100)
    dataLab = models.CharField(max_length=100)
    dataAdd = models.CharField(max_length=100)
    coclusion = models.CharField(max_length=100)
    date_record = models.DateField()
    next_date = models.DateField()