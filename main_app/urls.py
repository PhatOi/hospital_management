from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.main, name='homepage'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('add-medicine/', views.add_medicine, name='add-medicine'),
    path('remove-medicine/', views.remove_medicine, name='remove-medicine'),
    path('medicine-info/', views.medicine_info, name='medicine-info'),
    path('add-medical-equipment/', views.add_medical_equipment, name='add-medical-equipment'),
    path('medical-equipment-info/', views.medical_equipment_info, name='medical-equipment-info'),
]