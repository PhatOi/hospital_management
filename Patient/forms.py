from django import forms 
from .models import Patient, PersonalInfo
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 

class PatientForm (forms.ModelForm):
    class Meta:
        model = Patient 
        fields = '__all__'
        
class PersonalInfoForm (forms.ModelForm):
    class Meta:
        model = PersonalInfo
        fields = ['Name', 'Birthday', 'Nationality', 'Identity']
        
class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User 
        fields = ['username', 'email', 'password1', 'password2']