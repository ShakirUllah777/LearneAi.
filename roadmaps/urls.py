from django.urls import path
from .views import roadmap_list

urlpatterns = [
    path('', roadmap_list, name='roadmaps'),
]
