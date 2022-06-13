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
    stage=client.patientcard.prosthesis.stages_4
    config = {
        'client': client,
        'materials': a,
        'types': b,
        'constructions': c,
        'stage':stage
    }
    return render(request, 'stage4/index.html',config)

def update(request,id):
    client = Clients.objects.get(id=id)
    card = PatientCard.objects.get(client=client)
    card.status = 'Етап 4'
    card.save()
    stage=Stages_4.objects.get(id=client.patientcard.prosthesis.stages_4.id)
    if stage:
        stage.quality_compatib = request.POST['quality_compatib']
        stage.actions_perform = request.POST['actions_perform']
        stage.quality_instal = request.POST['quality_instal']
        stage.material_1 = request.POST['material_1']
        stage.material_2 = request.POST['material_2']
        stage.material_3 = request.POST['material_3']
        stage.material_4 = request.POST['material_4']

        stage.conclusion = request.POST['conclusion']
        stage.date_record = date.today()
        stage.save()
    return HttpResponseRedirect(reverse('stage4:index', kwargs={'id': id}))

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
                            f'Етап 4 - Примірка та встановлення протезу\n'
                            f'Якість сумістності протезу:{client.patientcard.prosthesis.stages_4.quality_compatib}\n'
                            f'Виконані дії для підлаштування протезу:{client.patientcard.prosthesis.stages_4.actions_perform}\n'
                            f'Якість встановленого протезу:{client.patientcard.prosthesis.stages_4.quality_instal}\n'
                            f'Материалы:{client.patientcard.prosthesis.stages_4.material_1}  '
                            f'{client.patientcard.prosthesis.stages_4.material_2}  '
                            f'{client.patientcard.prosthesis.stages_4.material_3}  '
                            f'{client.patientcard.prosthesis.stages_4.material_4}  \n'
                            f'Висновок:{ client.patientcard.prosthesis.stages_4.conclusion }')

        text_file.close()
        file_path = rf"c:\\prints\{file}.txt"
        os.system("start " + file_path)
    except:
        text_file.close()
    return HttpResponseRedirect(reverse('stage4:index', kwargs={'id': id}))