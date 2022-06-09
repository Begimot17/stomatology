from django.shortcuts import render
from django.urls import reverse
from .models import *
from django.http import HttpResponseRedirect


def index(request):
    a = Materials.objects.all()
    config = {
        'materials': a
    }
    return render(request, 'materials/index.html',config)\


def add(request):
    return render(request, 'materials/add.html')

def reg(request):
    material= Materials.objects.create(code=request.POST['code'],
                                   producer=request.POST['producer'],
                                  name=request.POST['name'],
                                  availability=request.POST['availability'],
                                  quality=request.POST['quality']
                                   )
    material.save()
    return HttpResponseRedirect(reverse('materials:index'))

def upd(request,id):
    material=Materials.objects.get(id=id)
    config={
        'material': material
    }
    return render(request, 'materials/update.html',config)
def update(request,id):
    material = Materials.objects.get(id=id)
    material.code = request.POST['code']
    material.producer = request.POST['producer']
    material.name = request.POST['name']
    material.availability = request.POST['availability']
    material.quality = request.POST['quality']
    material.save()
    return HttpResponseRedirect(reverse('materials:index'))

def delete(request, id):
    Materials.objects.get(id=id).delete()
    return HttpResponseRedirect(reverse('materials:index'))