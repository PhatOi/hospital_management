from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import SignUpForm, UserLoginForm
from .models import Facility, Medicine, MedicalEquipment

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

#-------------------------------------------
def add_medicine(request):
    if request.method == 'POST':
        medicine_name = request.POST.get('medicine_name')
        facility = Facility.objects.first()  # Lấy Facility (cần chỉnh sửa nếu có nhiều Facility)
        try:
            medicine = Medicine.objects.get(name=medicine_name)
            facility.add_medicine(medicine)
            return render(request, 'success.html', {'message': f"Đã thêm thuốc {medicine_name} vào Facility."})
        except Medicine.DoesNotExist:
            return render(request, 'error.html', {'message': f"Không tìm thấy thuốc có tên {medicine_name}."})
    else:
        return render(request, 'add_medicine.html')

def remove_medicine(request, medicine_name):
    try:
        medicine = Medicine.objects.get(name=medicine_name)
        facility = Facility.objects.first()  # Lấy Facility (cần chỉnh sửa nếu có nhiều Facility)
        facility.remove_medicine(medicine)
        return render(request, 'success.html', {'message': f"Đã xóa thuốc {medicine_name} khỏi Facility."})
    except Medicine.DoesNotExist:
        return render(request, 'error.html', {'message': f"Không tìm thấy thuốc có tên {medicine_name}."})    

def medicine_info(request):
    facility = Facility.objects.first()  # Lấy Facility (cần chỉnh sửa nếu có nhiều Facility)
    medicines = facility.get_medicines_info()
    return render(request, 'medicine_info.html', {'medicines': medicines})

def add_medical_equipment(request):
    if request.method == 'POST':
        # Lấy dữ liệu từ form gửi lên
        equipment_name = request.POST.get('equipment_name')
        # Thêm thiết bị y tế vào Facility
        facility = Facility.objects.first()  # Lấy Facility (cần chỉnh sửa nếu có nhiều Facility)
        try:
            equipment = MedicalEquipment.objects.get(name=equipment_name)
            facility.add_medical_equipment(equipment)
            return render(request, 'success.html', {'message': f"Đã thêm thiết bị y tế {equipment_name} vào Facility."})
        except MedicalEquipment.DoesNotExist:
            return render(request, 'error.html', {'message': f"Không tìm thấy thiết bị y tế có tên {equipment_name}."})
    else:
        # Hiển thị form để nhập thông tin thiết bị y tế
        return render(request, 'add_medical_equipment.html')

def medical_equipment_info(request):
    facility = Facility.objects.first()  # Lấy Facility (cần chỉnh sửa nếu có nhiều Facility)
    equipment = facility.get_medical_equipments_info()
    return render(request, 'medical_equipment_info.html', {'equipment': equipment})