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


    # HEALTHCARE STAFF
    path('healthcareStaff/homepage', views.healthcareStaff__Homepage, name='healthcareStaff__Homepage'),
    path('healthcareStaff/healthcareStaffInfor', views.healthcareStaff__Infor, name='healthcareStaff__Infor'),
    path('healthcareStaff/patient/infor', views.healthcareStaff__Patient_Infor, name='healthcareStaff__Patient_Infor'),
    path('healthcareStaff/patient/medicalHistory', views.healthcareStaff__Patient_MedicalHistory, name='healthcareStaff__Patient_MedicalHistory'),
    path('healthcareStaff/patient/testResult', views.healthcareStaff__Patient_TestResult, name='healthcareStaff__Patient_TestResult'),
    path('healthcareStaff/patient/schedule', views.healthcareStaff__Patient_Schedule, name='healthcareStaff__Patient_Schedule'),
    path('healthcareStaff/storage', views.healthcareStaff__Storage, name='healthcareStaff__Storage'),
    # HEALTHCARE STAFF

    # PATIENT
    path('Patient/Medical_History', views.Patient__Medical_History, name='Patient__Medical_History'),
    path('Patient/mainpage', views.Patient__MainPage, name='Patient__MainPage'),
    path('Patient/patient_info', views.Patient__Patient_Info, name='Patient__Patient_Info'),
    path('Patient/re-examination', views.Patient__Re_examination, name='Patient__Re_examination'),
    path('Patient/update_info', views.Patient__Update_Info, name='Patient__Update_Info'),
    path('Patient/login', views.Patient__Login, name='Patient__Login'),
    path('Patient/register', views.Patient__Register, name='Patient__Register'),
    path('Patient/forgot_password', views.Patient__Forgot_password, name='Patient__Forgot_password'),
    path('Patient/reset_password', views.Patient__Reset_password, name='Patient__Reset_password'),
    # PATIENT
]
