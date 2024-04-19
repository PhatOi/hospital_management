from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.loginPage, name='loginPage'),
    path('signup/', views.signupPage, name='signupPage'),
    path('forgotPassword/', views.forgotPasswordPage, name='forgotPasswordPage'),
    path('home/', views.main, name='homepage'),
    path('add-medicine/', views.add_medicine, name='add-medicine'),
    path('remove-medicine/', views.remove_medicine, name='remove-medicine'),
    path('medicine-info/', views.medicine_info, name='medicine-info'),
    path('add-medical-equipment/', views.add_medical_equipment, name='add-medical-equipment'),
    path('medical-equipment-info/', views.medical_equipment_info, name='medical-equipment-info'),

    # ADMIN
    path('hospital_admin', views.hospital_admin, name='hospital_admin'),
    # ADMIN

    # HEALTHCARE STAFF
    path('healthcareStaff/homepage', views.healthcareStaff__Homepage, name='healthcareStaff__Homepage'),
    path('healthcareStaff/healthcareStaffInfor', views.healthcareStaff__Infor, name='healthcareStaff__Infor'),
    path('healthcareStaff/mypatient/infor', views.healthcareStaff__Patient_Infor, name='healthcareStaff__Patient_Infor'),
    path('healthcareStaff/mypatient/medicalHistory', views.healthcareStaff__Patient_MedicalHistory, name='healthcareStaff__Patient_MedicalHistory'),
    path('healthcareStaff/mypatient/testResult', views.healthcareStaff__Patient_TestResult, name='healthcareStaff__Patient_TestResult'),
    path('healthcareStaff/mypatient/schedule', views.healthcareStaff__Patient_Schedule, name='healthcareStaff__Patient_Schedule'),
    path('healthcareStaff/storage', views.healthcareStaff__Storage, name='healthcareStaff__Storage'),
    # HEALTHCARE STAFF

    # NEW PATIENT
    path('patient/homepage', views.patient_home, name='patient_home'),
    path('patient/infor', views.patient_infor, name='patient_infor'),
    path('patient/medicalHistory', views.patient_medical_history, name='patient_medical_history'),
    path('patient/testResult', views.patient_test_result, name='patient_test_result'),
    path('patient/schedule', views.patient_schedule, name='patient_schedule'),
    # NEW PATIENT

    # PATIENT
    # path('Patient/Medical_History', views.Patient__Medical_History, name='Patient__Medical_History'),
    # path('Patient/mainpage', views.Patient__MainPage, name='Patient__MainPage'),
    # path('Patient/patient_info', views.Patient__Patient_Info, name='Patient__Patient_Info'),
    # path('Patient/re-examination', views.Patient__Re_examination, name='Patient__Re_examination'),
    # path('Patient/update_info', views.Patient__Update_Info, name='Patient__Update_Info'),
    # path('Patient/login', views.Patient__Login, name='Patient__Login'),
    # path('Patient/register', views.Patient__Register, name='Patient__Register'),
    # path('Patient/forgot_password', views.Patient__Forgot_password, name='Patient__Forgot_password'),
    # path('Patient/reset_password', views.Patient__Reset_password, name='Patient__Reset_password'),
    # PATIENT


    ########################## new url #######################################
    # path('main', views.main, name='HomePage'),
    # path('', views.LoginPage, name='LoginPage'),
    # path('doLogin', views.doLogin, name='doLogin'),
    # path('get_user_detail', views.getUserDetails, name='getUserDetails'),
    # path('logout_user', views.logout_user, name='logout'),

    # # admin
    # path('admin_home', admin_views.admin_home, name = 'adminhome'),
    # path('add_staff', admin_views.add_staff, name='addStaff'),
    # path('manage_staff', admin_views.manage_staff, name="manageAllStaff"),
    # path('add_patient', admin_views.add_patient, name='addPatient'),
    # path('manage_patient', admin_views.manage_patient, name="manageAllPatient"),
    # path('add_medicine', admin_views.add_medicine, name='add-medicine'),
    # path('manage_medicine', admin_views.manage_medicine, name="manageMedicine"),
    # path('add_medical_equipment', admin_views.add_medical_equipment, name='add-medical-equipment'),
    # path('manage_equip', admin_views.manage_equip, name="manageEquip"),
    # path('staff_feedback', admin_views.staff_feedback, name="staffAllFeedback"),
    # path('patient_feedback', admin_views.patient_feedback, name="patientAllFeedback"),
    # path('works', admin_views.work_schedules, name="workSchedules"),

    # # healthcare staff
    # path('staff/staff_home', healthcareStaff_views.staff_home, name="staffhome"),
    # path('staff/manage_staff/<int:staff_id>', healthcareStaff_views.manage_staff, name="manageStaff"),
    # path('staff/add_patient', healthcareStaff_views.add_patient, name='addPatient'),
    # path('staff/add_patient_save', healthcareStaff_views.add_patient_save, name='savePatient'),
    # path('staff/manage_patient', healthcareStaff_views.manage_patient, name="manageAllPatient"),
    # path('staff/add_medicine', healthcareStaff_views.add_medicine, name='add-medicine'),
    # path('staff/manage_medicine', healthcareStaff_views.manage_medicine, name="manageMedicine"),
    # path('staff/add_medical_equipment', healthcareStaff_views.add_medical_equipment, name='add-medical-equipment'),
    # path('staff/manage_equip', healthcareStaff_views.manage_equip, name="manageEquip"),
    # path('staff/staff_feedback/<int:staff_id>', healthcareStaff_views.staff_feedback, name="staffFeedback"),
    # path('staff/patient_feedback', healthcareStaff_views.patient_feedback, name="patientAllFeedback"),
    # path('staff/staff_calendar/<int:staff_id>', healthcareStaff_views.staff_calendar, name="staffCalendar"),

    # # Patient
    # path('patient/patient_home', patient_views.patient_home, name="patienthome"),
    # path('patient/manage_patient/<int:patient_id>', patient_views.manage_patient, name="managePatient"),
    # path('patient/patient_feedback/<int:patient_id>', patient_views.patient_feedback, name="patientFeedback"),
    # path('patient/patient_calendar/<int:patient_id>', patient_views.patient_calendar, name="patientCalendar"),
  
]
