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
    return render(request, 'stage1/index.html',config)
def update(request,id):
    client = Clients.objects.get(id=id)
    stage=Stages_1.objects.get(id=client.patientcard.prosthesis.stages_1.id)
    if stage:
        stage.complaints =request.POST['complaints']
        stage.diagnosis =request.POST['diagnosis']
        stage.disease_current =request.POST['disease_current']
        stage.progress_disease =request.POST['progress_disease']
        stage.review =request.POST['review']
        stage.bite =request.POST['bite']
        stage.color =request.POST['color']
        stage.conclusion =request.POST['conclusion']
        stage.date_record = date.today()
        stage.save()
    return HttpResponseRedirect(reverse('stage1:index', kwargs={'id': id}))