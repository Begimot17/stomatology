from django.shortcuts import render
from django.urls import reverse
from .models import *
from django.http import HttpResponseRedirect


def index(request):
    a = Materials.objects.all()
    config = {
        'materials': a
    }
    return render(request, 'materials/index.html',config)