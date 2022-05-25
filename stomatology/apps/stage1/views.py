from django.shortcuts import render

def index(request):
    return render(request, 'stage1/index.html')