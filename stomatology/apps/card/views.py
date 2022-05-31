from django.shortcuts import render
from django.urls import reverse
from .models import *
from patients.models import *
from materials.models import *
from django.http import HttpResponseRedirect


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
    return render(request, 'card/index.html',config)