from django.shortcuts import render
from django.urls import reverse
from .models import *
from patients.models import *
from django.http import HttpResponseRedirect
from materials.models import *

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
    return render(request, 'stage2/index.html',config)


def update(request,id):
    client = Clients.objects.get(id=id)
    stage=Stages_2.objects.get(id=client.patientcard.prosthesis.stages_2.id)
    if stage:
        stage.conclusion = request.POST['conclusion']
        stage.date_record = date.today()
        stage.save()
    return HttpResponseRedirect(reverse('stage2:index', kwargs={'id': id}))