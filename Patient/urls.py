from django.urls import path, include 
from . import views


urlpatterns = [
    path('patient_create/', views.patient_create, name = 'patient_create'),
    path('person/', views.person, name = 'person'),
    #path('login_account/', views.loginPage, name = 'login'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]