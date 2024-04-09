from django.urls import path
from . import views


urlpatterns = [
    path('patient_create/', views.patient_create, name = 'patient_create'),
    path('person/', views.person, name = 'person'),
    path('login_account/', views.loginPage, name = 'login'),
    path('logout_account/', views.logoutUser, name = 'logout'),
    path('register_account/', views.registerUser, name = 'register'),
]