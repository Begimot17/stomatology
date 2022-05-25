from django.db import models
from card.models import Prosthesis

class Stages_1(models.Model):
    prosthesis = models.ForeignKey(Prosthesis, on_delete=models.CASCADE)
    complaints = models.CharField(max_length=100)
    diagnosis = models.CharField(max_length=100)
    disease_current = models.CharField(max_length=100)
    progress_disease = models.CharField(max_length=100)
    review = models.CharField(max_length=100)
    bite = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    conclusion = models.CharField(max_length=100)
    date_record = models.DateField()
    next_date = models.DateField()
