from django.contrib.auth import authenticate, login, logout, get_user_model
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from .models import *
from materials.models import *
from card.models import *
from stage1.models import *
from stage2.models import *
from stage3.models import *
from stage4.models import *
from datetime import date



def index(request):
    a = Clients.objects.all()
    config = {
        'clients': a
    }
    return render(request, 'patients/index.html',config)
def add(request):
    a = Materials.objects.all()
    b = Type_prost.objects.all()
    c = Construction.objects.all()
    config = {
        'materials': a,
        'types': b,
        'constructions': c
    }
    return render(request, 'patients/add.html',config)

def reg(request):
    UserModel = get_user_model()
    user = UserModel.objects.create_user(username=(request.POST['first_name']+request.POST['last_name']+request.POST['phone']), password='root')
    user.first_name = request.POST['first_name']
    user.last_name = request.POST['last_name']
    user.save()

    client= Clients.objects.create(user=user,phone=request.POST['phone'],
                                  gender=request.POST['gender'],
                                  date_birth=request.POST['date_birth'])
    client.save()
    patientcard = PatientCard.objects.create(client=client)
    patientcard.status = 'Новий пацієнт'
    patientcard.save()

    prosthesis = Prosthesis.objects.create(card=patientcard)
    prosthesis.save()
    stage1=Stages_1.objects.create(prosthesis=prosthesis)
    stage1.save()
    stage2 = Stages_2.objects.create(prosthesis=prosthesis)
    stage2.save()
    stage3 = Stages_3.objects.create(prosthesis=prosthesis)
    stage3.save()
    stage4 = Stages_4.objects.create(prosthesis=prosthesis)
    stage4.save()
    return HttpResponseRedirect(reverse('patients:index'))


def update(request,id):
    client = Clients.objects.get(id=id)
    user = client.user
    user.last_name = request.POST['last_name']
    user.first_name = request.POST['first_name']
    user.save()
    client.phone = request.POST['phone']
    client.gender = request.POST['gender']
    client.date_birth = request.POST['date_birth']
    card=client.patientcard
    card.status= request.POST['status']
    card.save()
    prosthesis=client.patientcard.prosthesis
    prosthesis.material= Materials.objects.get(id=request.POST['material'])
    prosthesis.type = Type_prost.objects.get(id=request.POST['type'])
    prosthesis.construction = Construction.objects.get(id=request.POST['construction'])
    client.save()
    prosthesis.save()
    return HttpResponseRedirect(reverse('patients:index'))

def delete(request, id):
    Clients.objects.get(id=id).delete()
    return HttpResponseRedirect(reverse('patients:index'))