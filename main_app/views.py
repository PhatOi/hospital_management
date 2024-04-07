from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import SignUpForm, UserLoginForm

def main(request):
    template = loader.get_template("main.html")
    return HttpResponse(template.render())    

# HEALTHCARE STAFF
def healthcareStaff__Homepage(request):
    template = loader.get_template("HealthcareStaff/homePage.html")
    return HttpResponse(template.render())    

def healthcareStaff__Infor(request):
    template = loader.get_template("HealthcareStaff/healthcareStaffInfor.html")
    return HttpResponse(template.render())    

def healthcareStaff__Patient(request):
    template = loader.get_template("HealthcareStaff/patient.html")
    return HttpResponse(template.render())   

def healthcareStaff__Patient_Infor(request):
    template = loader.get_template("HealthcareStaff/patient/infor.html")
    return HttpResponse(template.render())   

def healthcareStaff__Patient_MedicalHistory(request):
    template = loader.get_template("HealthcareStaff/patient/medicalHistory.html")
    return HttpResponse(template.render())   

def healthcareStaff__Patient_TestResult(request):
    template = loader.get_template("HealthcareStaff/patient/testResult.html")
    return HttpResponse(template.render())   

def healthcareStaff__Patient_Schedule(request):
    template = loader.get_template("HealthcareStaff/patient/schedule.html")
    return HttpResponse(template.render()) 
  
def healthcareStaff__Storage(request):
    template = loader.get_template("HealthcareStaff/storage.html")
    return HttpResponse(template.render()) 
# HEALTHCARE STAFF

# PATIENT
def Patient__Medical_History(request):
    template = loader.get_template("Patient/Medical_History.html")
    return HttpResponse(template.render()) 

def Patient__MainPage(request):
    template = loader.get_template("Patient/mainpage.html")
    return HttpResponse(template.render()) 

def Patient__Patient_Info(request):
    template = loader.get_template("Patient/patient_info.html")
    return HttpResponse(template.render()) 

def Patient__Re_examination(request):
    template = loader.get_template("Patient/re-examination.html")
    return HttpResponse(template.render()) 

def Patient__Update_Info(request):
    template = loader.get_template("Patient/update_info.html")
    return HttpResponse(template.render()) 

def Patient__Login(request):
    template = loader.get_template("Patient/login.html")
    return HttpResponse(template.render()) 

def Patient__Register(request):
    template = loader.get_template("Patient/register.html")
    return HttpResponse(template.render()) 

def Patient__Forgot_password(request):
    template = loader.get_template("Patient/forgot_password.html")
    return HttpResponse(template.render()) 

def Patient__Reset_password(request):
    template = loader.get_template("Patient/reset_password.html")
    return HttpResponse(template.render()) 
# PATIENT

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('homepage')  # Thay 'home' bằng tên đường dẫn của trang chính sau khi đăng ký thành công
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('homepage')  # Thay 'home' bằng tên đường dẫn của trang chính sau khi đăng nhập thành công
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('homepage')  # Thay 'home' bằng tên đường dẫn của trang chính sau khi đăng xuất thành công
