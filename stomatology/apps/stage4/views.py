from django.shortcuts import render

def index(request):
    return render(request, 'stage4/index.html')