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
    return render(request, 'stage3/index.html',config)

def update(request,id):
    client = Clients.objects.get(id=id)
    card = PatientCard.objects.get(client=client)
    card.status = 'Етап 3'
    card.save()
    stage=Stages_3.objects.get(id=client.patientcard.prosthesis.stages_3.id)
    if stage:
        stage.course_treatment = request.POST['course_treatment']
        stage.diagnosis_fin = request.POST['diagnosis_fin']
        stage.quality_cast = request.POST['quality_cast']
        stage.description = request.POST['description']
        stage.conclusion = request.POST['conclusion']
        stage.date_record = date.today()
        stage.save()
    return HttpResponseRedirect(reverse('stage3:index', kwargs={'id': id}))

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
                            f'Етап 3 - Обрання протезу та створення зліпку\n'
                            f'Призначення курсу лікування:{client.patientcard.prosthesis.stages_3.course_treatment}\n'
                            f'Остаточна постановка діагнозу:{client.patientcard.prosthesis.stages_3.diagnosis_fin}\n'
                            f'Якість створеного зліпку:{client.patientcard.prosthesis.stages_3.quality_cast}\n'
                            f'Додатковий опис:{client.patientcard.prosthesis.stages_3.description}\n'
                            f'Висновок:{ client.patientcard.prosthesis.stages_3.conclusion }')

        text_file.close()
        file_path = rf"c:\\prints\{file}.txt"
        os.system("start " + file_path)
    except:
        text_file.close()
    return HttpResponseRedirect(reverse('stage3:index', kwargs={'id': id}))