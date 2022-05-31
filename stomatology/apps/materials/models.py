from django.db import models


class Materials(models.Model):
    code = models.CharField(max_length=100)
    producer = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    availability = models.IntegerField()
    quality = models.IntegerField()


class Type_prost(models.Model):
    name = models.CharField(max_length=100)


class Construction(models.Model):
    name = models.CharField(max_length=100)


