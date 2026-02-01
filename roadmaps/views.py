from django.shortcuts import render
from .models import Roadmap

def roadmap_list(request):
    data = Roadmap.objects.all()
    return render(request, 'roadmaps.html', {'roadmaps': data})
