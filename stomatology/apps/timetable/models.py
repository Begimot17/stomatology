from django.db import models
from card.models import PatientCard
from authorize.models import Doctors


class Schedule(models.Model):
    doctor= models.ForeignKey(Doctors, on_delete=models.CASCADE)
    patient_card = models.ForeignKey(PatientCard, on_delete=models.CASCADE)
    date_birth = models.CharField(max_length=100)

