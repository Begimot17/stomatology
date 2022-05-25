from django.shortcuts import render

def index(request):
    return render(request, 'stage3/index.html')