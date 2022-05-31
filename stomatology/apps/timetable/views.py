from django.shortcuts import render
from django.urls import reverse
from .models import *
from django.http import HttpResponseRedirect


def index(request):
    a = Schedule.objects.all()
    config = {
        'schedules': a
    }
    return render(request, 'timetable/index.html',config)