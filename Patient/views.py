from django.shortcuts import render, redirect
from .forms import PatientForm, PersonalInfoForm 
from django.contrib.auth.models import User 
from django.contrib import messages 
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.forms import UserCreationForm

def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('homepage')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username = username)
        except:
            messages.error(request, 'User does not exist')
            
        authenticated_user = authenticate(request, username=username, password=password)
        if authenticated_user is not None: 
            login(request, authenticated_user)
            return redirect('homepage')
        else: 
             messages.error(request, 'Username or password does not exist!')
    context = {'page': page}
    return render (request, 'login_register.html', context)


def logoutUser(request):
    logout(request) 
    return redirect('login')

def registerUser(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save( commit = False)
            user.save()
            login(request, user)
            return redirect ('homepage')
        else:
            messages.error(request, 'An error occur!')
    context= {'form': form}
    return render(request, 'login_register.html', context)


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
