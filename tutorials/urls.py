from django.urls import path
from .views import tutorial_list

urlpatterns = [
    path('', tutorial_list, name='tutorials'),
]
