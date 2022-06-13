from django.shortcuts import render
from django.urls import reverse
from .models import *
from patients.models import *
from django.http import HttpResponseRedirect
from materials.models import *
from datetime import date
from card.models import *
import time
import os

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
    card = PatientCard.objects.get(client=client)
    card.status = 'Етап 2'
    card.save()
    stage=Stages_2.objects.get(id=client.patientcard.prosthesis.stages_2.id)
    if stage:
        stage.conclusion = request.POST['conclusion']
        stage.date_record = date.today()
        stage.save()
    return HttpResponseRedirect(reverse('stage2:index', kwargs={'id': id}))


def print_info(request,id):
    file = str(time.time())
    try:
        client = Clients.objects.get(id=id)
        text_file = open(rf"c:\\prints\{file}.txt", "w")
        n = text_file.write(f'Прізвище:{ client.user.last_name }\n'
                            f'Ім\'я:{ client.user.first_name }\n'
                            f'Телефон:{ client.phone }\n'
                            f'Дата народження:{client.date_birth}\n'
                            f'Тип протезування:{client.patientcard.prosthesis.type.name}\n'
                            f'Конструкція:{client.patientcard.prosthesis.construction.name}\n'
                            f'Матеріал:{client.patientcard.prosthesis.material.name}\n'
                            f'Стать:{client.gender}\n'
                            f'Етап 2 - Додаткові дослідження\n'
                            f'Висновок:{ client.patientcard.prosthesis.stages_2.conclusion }')


        file_path = rf"c:\\prints\{file}.txt"
        os.system("start " + file_path)
        text_file.close()
    except:
        text_file.close()
    return HttpResponseRedirect(reverse('stage2:index', kwargs={'id': id}))