from django.shortcuts import render
from django.urls import reverse
from .models import *
from patients.models import *
from django.http import HttpResponseRedirect
from materials.models import *
from datetime import date


def index(request,id):
    client = Clients.objects.get(id=id)
    a = Materials.objects.all()
    b = Type_prost.objects.all()
    c = Construction.objects.all()
    config = {
        'client': client,
        'materials': a,
        'types': b,
        'constructions': c
    }
    return render(request, 'stage3/index.html',config)

def update(request,id):
    client = Clients.objects.get(id=id)
    stage=Stages_3.objects.get(id=client.patientcard.prosthesis.stages_3.id)
    if stage:
        stage.course_treatment = request.POST['course_treatment']
        stage.diagnosis_fin = request.POST['diagnosis_fin']
        stage.quality_cast = request.POST['quality_cast']
        stage.description = request.POST['description']
        stage.conclusion = request.POST['conclusion']
        stage.date_record = date.today()
        stage.save()
    return HttpResponseRedirect(reverse('stage3:index', kwargs={'id': id}))