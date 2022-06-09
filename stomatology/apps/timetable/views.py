from django.shortcuts import render
from django.urls import reverse
from .models import *
from card.models import *
from authorize.models import *
from django.http import HttpResponseRedirect


def index(request):
    a = Schedule.objects.all()
    config = {
        'schedules': a
    }
    return render(request, 'timetable/index.html',config)


def add(request):
    doctors = Doctors.objects.all()
    cards = PatientCard.objects.all()
    config={
        'doctors':doctors,
        'cards':cards
    }
    return render(request, 'timetable/add.html',config)

def reg(request):
    schedule= Schedule.objects.create(doctor=Doctors.objects.get(id=request.POST['doctor']),
                                   patient_card=PatientCard.objects.get(id=request.POST['patient_card']),
                                  date_birth=request.POST['date_birth'].replace('T',' ')
                                   )
    schedule.save()
    return HttpResponseRedirect(reverse('timetable:index'))

def upd(request,id):
    timetable=Schedule.objects.get(id=id)
    doctors = Doctors.objects.all()
    cards = PatientCard.objects.all()
    time=timetable.date_birth.replace(' ','T')
    config = {
        'doctors': doctors,
        'cards': cards,
        'timetable': timetable,
        'time':time
    }
    return render(request, 'timetable/update.html',config)
def update(request,id):
    timetable = Schedule.objects.get(id=id)
    timetable.doctor = Doctors.objects.get(id=request.POST['doctor'])
    timetable.patient_card = PatientCard.objects.get(id=request.POST['patient_card'])
    timetable.date_birth = request.POST['date_birth'].replace('T',' ')
    timetable.save()
    return HttpResponseRedirect(reverse('timetable:index'))

def delete(request, id):
    Schedule.objects.get(id=id).delete()
    return HttpResponseRedirect(reverse('timetable:index'))