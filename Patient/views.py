from django.shortcuts import render, redirect
from .forms import PatientForm, PersonalInfoForm 

def patient_create (request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')  # Điều hướng đến trang thành công sau khi lưu form
    else:
        form = PatientForm()
    return render(request, 'create_patient.html', {'form': form})

def person (request):
    if request.method == 'POST':
        form = PersonalInfoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = PersonalInfoForm() 
    return render(request, 'person.html', {'form': form})

# Create your views here.
