from django.shortcuts import render
from .models import About

def home(request):
    return render(request, 'home.html')

def about(request):
    data = About.objects.first()
    return render(request, 'about.html', {'about': data})
