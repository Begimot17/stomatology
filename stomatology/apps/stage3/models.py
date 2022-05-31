from django.db import models

from  card.models import Prosthesis

class Stages_3(models.Model):
    prosthesis = models.OneToOneField(Prosthesis, on_delete=models.CASCADE)
    course_treatment = models.CharField(max_length=100)
    diagnosis_fin = models.CharField(max_length=100)
    quality_cast = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    conclusion = models.CharField(max_length=100)
    date_record = models.DateField(null=True)
    next_date = models.DateField(null=True)
