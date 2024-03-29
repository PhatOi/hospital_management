from django.urls import path
from . import views


urlpatterns = [
    path('patient_create/', views.patient_create, name = 'patient_create'),
    path('person/', views.person, name = 'person'),
]