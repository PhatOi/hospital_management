from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import SignUpForm, UserLoginForm
from .models import Facility, Medicine, MedicalEquipment, MedicineHistory

def main(request):
    return render(request, 'main.html')  

def home(request):
    return render(request, 'home.html')

def loginPage(request):
    return render(request,'login.html')

def signupPage(request):
    return render(request, 'signup.html')

def forgotPasswordPage(request):
    return render(request, 'forgotpassword.html')

# ADMIN
def hospital_admin(request):
    template = loader.get_template("admin/admin.html")
    return HttpResponse(template.render())  
# ADMIN



# HEALTHCARE STAFF
def healthcareStaff__Homepage(request):
    template = loader.get_template("Staff/homePage.html")
    return HttpResponse(template.render())    

def healthcareStaff__Infor(request):
    template = loader.get_template("Staff/staffInfor.html")
    return HttpResponse(template.render())    

def healthcareStaff__Patient_Infor(request):
    template = loader.get_template("Staff/pages/patient/infor.html")
    return HttpResponse(template.render())   

def healthcareStaff__Patient_MedicalHistory(request):
    template = loader.get_template("Staff/pages/patient/medicalHistory.html")
    return HttpResponse(template.render())   

def healthcareStaff__Patient_TestResult(request):
    template = loader.get_template("Staff/pages/patient/generalTestResults.html")
    return HttpResponse(template.render())   

def healthcareStaff__Patient_Schedule(request):
    template = loader.get_template("Staff/pages/patient/medicalExaminationSchedule.html")
    return HttpResponse(template.render()) 
  
def healthcareStaff__Storage(request):
    template = loader.get_template("Staff/medicineFacilities.html")
    return HttpResponse(template.render()) 
# HEALTHCARE STAFF



# NEW PATIENT TEMPLATE
def patient_home(request):
    template = loader.get_template("newpatient/homePage.html")
    return HttpResponse(template.render())  
    
def patient_infor(request):
    template = loader.get_template("newpatient/infor.html")
    return HttpResponse(template.render())  

def patient_medical_history(request):
    template = loader.get_template("newpatient/medicalHistory.html")
    return HttpResponse(template.render())  

def patient_test_result(request):
    template = loader.get_template("newpatient/generalTestResults.html")
    return HttpResponse(template.render())  

def patient_schedule(request):
    template = loader.get_template("newpatient/medicalExaminationSchedule.html")
    return HttpResponse(template.render())  
# NEW PATIENT TEMPLATE



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

#-------------------------------------------
