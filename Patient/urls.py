from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('create_profile/', views.create_profile, name = 'create_profile'),
    path('view_profile/', views.view_profile, name='view_profile'),
    path('edit_profile/', views.edit_profile, name = 'edit_profile'),
    path('send_feedback/', views.send_feedback, name = 'send_feedback'),
    path('view_feedback/', views.view_feedback, name = 'view_feedback'),
    path('view_medical_date/', views.medical_history, name = 'medical_history'),
    path('view_testResult', views.view_testResult, name = 'test_result'),
]