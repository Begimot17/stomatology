from django.shortcuts import render
from django.urls import reverse
from .models import *
from card.models import *
from patients.models import *
from django.http import HttpResponseRedirect
from materials.models import *
from datetime import date
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
    return render(request, 'stage1/index.html',config)
def update(request,id):
    client = Clients.objects.get(id=id)
    card=PatientCard.objects.get(client=client)
    card.status='Етап 1'
    card.save()
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
                            f'Етап 1 - Первичний огляд та визначення плану\n'
                            f'Скарги:{client.patientcard.prosthesis.stages_1.complaints}\n'
                            f'Діагноз:{client.patientcard.prosthesis.stages_1.diagnosis}\n'
                            f'Перенесені та супутні захворювання:{ client.patientcard.prosthesis.stages_1.disease_current }\n'
                            f'Розвиток захворювання:{ client.patientcard.prosthesis.stages_1.progress_disease }\n'
                            f'Дані об\'єктивного дослідження:{ client.patientcard.prosthesis.stages_1.review }\n'
                            f'Прикус:{ client.patientcard.prosthesis.stages_1.bite }\n'
                            f'Колір за шкалою \'Віта\':{ client.patientcard.prosthesis.stages_1.color }\n'
                            f'Висновок:{ client.patientcard.prosthesis.stages_1.conclusion }')
        text_file.close()
        file_path = rf"c:\\prints\{file}.txt"
        os.system("start " + file_path)

    except:
        text_file.close()
    return HttpResponseRedirect(reverse('stage1:index', kwargs={'id': id}))