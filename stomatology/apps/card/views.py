from django.shortcuts import render
from django.urls import reverse
from .models import *
from patients.models import *
from materials.models import *
from django.http import HttpResponseRedirect
import time
import os

def index(request,id):
    client = Clients.objects.get(id=id)
    card=PatientCard.objects.get(client=client)
    prothesis=Prosthesis.objects.get(card=card)
    a = Materials.objects.all()
    b = Type_prost.objects.all()
    c = Construction.objects.all()
    config = {
        'client': client,
        'materials': a,
        'types': b,
        'constructions': c,
        'prothesis':prothesis
    }
    return render(request, 'card/index.html',config)


def print_info(request,id):
    file=str(time.time())
    try:
        client = Clients.objects.get(id=id)
        print(client)
        card = PatientCard.objects.get(client=client)
        print(card)
        prothesis = Prosthesis.objects.get(card=card)
        print(prothesis)
        text_file = open(rf"c:\\prints\{file}.txt", "w")
        n = text_file.write(f'Прізвище:{ client.user.last_name }\n'
                            f'Ім\'я:{ client.user.first_name }\n'
                            f'Телефон:{ client.phone }\n'
                            f'Дата народження:{client.date_birth}\n'
                            f'Тип протезування:{client.patientcard.prosthesis.type.name}\n'
                            f'Конструкція:{client.patientcard.prosthesis.construction.name}\n'
                            f'Матеріал:{client.patientcard.prosthesis.material.name}\n'
                            f'Стать:{client.gender}\n'
                            f'Етапи лікування\n'
                            f'Етап 1/{prothesis.stages_1.date_record}:{prothesis.stages_1.conclusion}\n'
                            f'Етап 2/{prothesis.stages_2.date_record}:{prothesis.stages_2.conclusion}\n'
                            f'Етап 3/{prothesis.stages_3.date_record}:{prothesis.stages_3.conclusion}\n'
                            f'Етап 4/{prothesis.stages_4.date_record}:{prothesis.stages_4.conclusion}\n')

        print(n)
        text_file.close()
        file_path = rf'C:\\prints\{file}.txt'
        os.system("start " + file_path)
    except:
        text_file.close() 
    return HttpResponseRedirect(reverse('card:index', kwargs={'id': id}))


