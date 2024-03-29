from django import forms 
from .models import Patient, PersonalInfo

class PatientForm (forms.ModelForm):
    class Meta:
        model = Patient 
        fields = '__all__'
        
class PersonalInfoForm (forms.ModelForm):
    class Meta:
        model = PersonalInfo
        fields = ['Name', 'Birthday', 'Nationality', 'Identity']