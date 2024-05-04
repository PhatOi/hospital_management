from django.urls import path, include
from . import views, admin_views, healthcareStaff_views, patient_views

urlpatterns = [
    # path('main', views.main, name='home_page'),
    path('', views.login_page, name='login_page'),
    path('doLogin', views.do_login, name='do_login'),
    path('accounts', include('django.contrib.auth.urls')),
    path('logout_user', views.logout_user, name='logout'),

    # admin
    path('admin_home', admin_views.admin_home, name = 'admin_home'),
    path('admin_profile', admin_views.admin_profile, name = 'admin_profile'),
    path('add_staff', admin_views.add_staff, name='add_staff'),
    path('manage_staff', admin_views.manage_staff, name="manage_all_staff"),
    path('edit_staff/<str:staff_id>', admin_views.edit_staff, name="edit_staff"),
    path('delete_staff/<str:staff_id>', admin_views.delete_staff, name="delete_staff"),
    

    path('add_patient', admin_views.add_patient, name='add_patient'),
    path('manage_patient', admin_views.manage_patient, name="manage_all_patient"),
    path('edit_patient/<str:patient_id>', admin_views.edit_patient, name="edit_patient"),
    path('test_result/<str:patient_id>', admin_views.test_result, name="test_result"),
    path('medical_history/<str:patient_id>', admin_views.medical_history, name="medical_history"),
    path('delete_patient/<str:patient_id>', admin_views.delete_patient, name="delete_patient"),
    path('check_email_exist', admin_views.check_email_exist, name="check_email_exist"),
    

    path('add_medicine', admin_views.add_medicine, name='add_medicine'),
    path('manage_medicine', admin_views.manage_medicine, name="manage_medicine"),
    path('medicine_history', admin_views.medicine_history, name='medicine_history'),
    path('edit_medicine/<str:medicine_id>', admin_views.edit_medicine, name="edit_medicine"),
    path('remove_medicine/<str:medicine_id>', admin_views.remove_medicine, name="remove_medicine"),
    

    path('add_medical_equipment', admin_views.add_medical_equipment, name='add_medical_equipment'),
    path('manage_equip', admin_views.manage_equip, name="manage_equip"),
    path('edit_medical_equipment/<str:equip_id>', admin_views.edit_medical_equipment, name="edit_medical_equipment"),
    path('remove_medical_equipment/<str:equip_id>', admin_views.remove_medical_equipment, name="remove_medical_equipment"),
    path('maintenance_history', admin_views.maintenance_history, name="maintenance_history"),    
    path('maintenance/<str:equip_id>', admin_views.maintain_equip, name="maintain_equip"),    
    

    path('staff_feedback', admin_views.staff_feedback, name="staff_all_feedback"),
    path('patient_feedback', admin_views.patient_feedback, name="patient_all_feedback"),

    path('add_event', admin_views.add_event, name='add_event'),
    path('works', admin_views.work_schedules, name="work_schedules"),
    path('staff_of_facilities/<str:facility_id>', admin_views.staff_of_facilities, name='staff_of_facilities'),
    path('patient_medical_info/<str:patient_id>', admin_views.patient_medical_info, name='patient_medical_info'),
    path('delete_event/<str:event_id>', admin_views.delete_event, name='delete_event'),
    path('edit_event', admin_views.edit_event, name='edit_event'),
    path('check_staff_available', admin_views.check_staff_available, name='check_staff_available'),
    


    # healthcare staff
    path('staff/staff_home', healthcareStaff_views.staff_home, name="staff_home"),
    path('staff/staff_profile', healthcareStaff_views.staff_profile, name="staff_profile"),
    path('staff/check_email_exist', healthcareStaff_views.check_email_exist),

    path('staff/add_patient', healthcareStaff_views.add_patient, name='staff_add_patient'),
    path('staff/manage_patient', healthcareStaff_views.manage_patient, name="staff_manage_patient"),
    path('staff/edit_patient/<str:patient_id>', healthcareStaff_views.edit_patient, name="staff_edit_patient"),
    path('staff/test_result/<str:patient_id>', healthcareStaff_views.test_result, name="staff_add_test_result"),
    path('staff/medical_history/<str:patient_id>', healthcareStaff_views.medical_history, name="staff_add_medical_history"),


    path('staff/add_medicine', healthcareStaff_views.add_medicine, name='staff_add_medicine'),
    path('staff/manage_medicine', healthcareStaff_views.manage_medicine, name="staff_manage_medicine"),
    path('staff/medicine_history', healthcareStaff_views.medicine_history, name='view_medicine_history'),
    path('staff/edit_medicine/<str:medicine_id>', healthcareStaff_views.edit_medicine, name="staff_edit_medicine"),
    path('staff/remove_medicine/<str:medicine_id>', healthcareStaff_views.remove_medicine, name="staff_remove_medicine"),

    path('staff/add_medical_equipment', healthcareStaff_views.add_medical_equipment, name='staff_add_medical_equipment'),
    path('staff/manage_equip', healthcareStaff_views.manage_equip, name="staff_manage_equip"),
    path('staff/edit_medical_equipment/<str:equip_id>', healthcareStaff_views.edit_medical_equipment, name="staff_edit_medical_equipment"),
    path('staff/remove_medical_equipment/<str:equip_id>', healthcareStaff_views.remove_medical_equipment, name="staff_remove_medical_equipment"),
    path('staff/maintenance_history', healthcareStaff_views.maintenance_history, name="view_maintenance_history"),    
    path('staff/maintenance/<str:equip_id>', healthcareStaff_views.maintain_equip, name="staff_maintain_equip"),    

    path('staff/staff_calendar', healthcareStaff_views.staff_calendar, name="staff_calendar"),
    path('staff/staff_feedback', healthcareStaff_views.staff_feedback, name="staff_feedback"),
    path('staff/patient_feedback', healthcareStaff_views.patient_feedback, name="follow-up_patient_feedback"),

    # Patient
    path('patient/patient_home', patient_views.patient_home, name="patient_home"),
    path('patient/patient_profile', patient_views.patient_profile, name="patient_profile"),
    path('patient/test_result', patient_views.test_result, name="patient_test_result"),
    path('patient/medical_history', patient_views.medical_history, name="patient_medical_history"),
    path('patient/check_email_exist', patient_views.check_email_exist),

    path('patient/patient_feedback', patient_views.patient_feedback, name="patient_feedback"),

    path('patient/patient_calendar', patient_views.patient_calendar, name="patient_calendar"),
]
