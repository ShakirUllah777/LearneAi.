from django.shortcuts import render
from .models import Tutorial

def tutorial_list(request):
    data = Tutorial.objects.all()
    return render(request, 'tutorials.html', {'tutorials': data})
