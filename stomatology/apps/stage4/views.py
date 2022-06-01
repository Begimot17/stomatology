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
    return render(request, 'stage4/index.html',config)