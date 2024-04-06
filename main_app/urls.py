from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.main, name='homepage'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),

    # HEALTHCARE STAFF
    path('healthcareStaff/homepage', views.healthcareStaff__Homepage, name='healthcareStaff__Homepage'),
    path('healthcareStaff/healthcareStaffInfor', views.healthcareStaff__Infor, name='healthcareStaff__Infor'),
    path('healthcareStaff/patient', views.healthcareStaff__Patient, name='healthcareStaff__Patient'),
    path('healthcareStaff/patient/infor', views.healthcareStaff__Patient_Infor, name='healthcareStaff__Patient_Infor'),
    path('healthcareStaff/patient/medicalHistory', views.healthcareStaff__Patient_MedicalHistory, name='healthcareStaff__Patient_MedicalHistory'),
    path('healthcareStaff/patient/testResult', views.healthcareStaff__Patient_TestResult, name='healthcareStaff__Patient_TestResult'),
    path('healthcareStaff/patient/schedule', views.healthcareStaff__Patient_Schedule, name='healthcareStaff__Patient_Schedule'),
    path('healthcareStaff/storage', views.healthcareStaff__Storage, name='healthcareStaff__Storage'),
    # HEALTHCARE STAFF

]