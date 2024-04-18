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
        medicine_numbers = int(request.POST.get('medicine_numbers'))
        medicine_expiry = request.POST.get('medicine_expiry')
        facility = Facility.objects.first()  # Lấy Facility (cần chỉnh sửa nếu có nhiều Facility)
        if facility == None: 
            facility = Facility.objects.create()

        try:
            medicine = Medicine.objects.get(name=medicine_name)
            medicine.numbers += medicine_numbers
            medicine.save()
            MedicineHistory.objects.create(name=medicine.name, numbers=medicine_numbers, changeType='import')
            return render(request, 'success.html', {'message': f"Đã thêm {medicine_numbers} thuốc {medicine_name} vào Facility."})
        except Medicine.DoesNotExist:
            new_medicine = Medicine.objects.create(name=medicine_name, numbers=medicine_numbers, expiry=medicine_expiry)
            facility.add_medicine(new_medicine)
            MedicineHistory.objects.create(name=new_medicine.name, numbers=new_medicine.numbers, changeType='import')
            return render(request, 'success.html', {'message': f"Đã thêm thuốc mới {medicine_name} vào Facility."})
    else:
        return render(request, 'add_medicine.html')

def remove_medicine(request, medicine_name):
    if request.method == 'POST':
        medicine_name = request.POST.get('medicine_name')
        medicine_numbers = int(request.POST.get('medicine_numbers'))
        try:
            medicine = Medicine.objects.get(name=medicine_name)
            if medicine.numbers > medicine_numbers:
                medicine.numbers -= medicine_numbers
                medicine.save()
                MedicineHistory.objects.create(name=medicine.name, numbers=medicine.numbers, changeType='export')
                return render(request, 'success.html', {'message': f"Đã giảm {medicine_numbers} thuốc {medicine_name} khỏi Facility."})
            elif medicine.numbers == medicine_numbers:
                medicine.numbers = 0
                medicine.save()
                MedicineHistory.objects.create(name=medicine.name, numbers=0, changeType='export')
                return render(request, 'success.html', {'message': f"Đã giảm hết số lượng thuốc {medicine_name} khỏi Facility."})
            else:
                return render(request, 'error.html', {'message': f"Số lượng thuốc {medicine_name} trong Facility không đủ."})
        except Medicine.DoesNotExist:
            return render(request, 'error.html', {'message': f"Không tìm thấy thuốc có tên {medicine_name}."})
    else:
        return render(request, 'remove_medicine.html')

def medicine_info(request):
    facility = Facility.objects.first()  # Lấy Facility (cần chỉnh sửa nếu có nhiều Facility)
    if facility == None: 
        facility = Facility.objects.create()    
    medicines = facility.get_medicines_info()
    return render(request, 'medicine_info.html', {'medicines': medicines})

def add_medical_equipment(request):
    if request.method == 'POST':
        equipment_name = request.POST.get('equipment_name')
        equipment_numbers = int(request.POST.get('equipment_numbers'))
        facility = Facility.objects.first()  # Lấy Facility (cần chỉnh sửa nếu có nhiều Facility)
        if facility == None: 
            facility = Facility.objects.create()

        try:
            equipment = MedicalEquipment.objects.get(name=equipment_name)
            equipment.numbers += equipment_numbers
            equipment.save()
            return render(request, 'success.html', {'message': f"Đã thêm {equipment_numbers} thiết bị y tế {equipment_name} vào Facility."})
        except MedicalEquipment.DoesNotExist:
            new_equipment = MedicalEquipment.objects.create(name=equipment_name, numbers=equipment_numbers)
            facility.add_medical_equipment(new_equipment)
            return render(request, 'success.html', {'message': f"Đã thêm thiết bị y tế mới {equipment_name} vào Facility."})
    else:
        return render(request, 'add_medical_equipment.html')

def remove_medical_equipment(request):
    if request.method == 'POST':
        equipment_name = request.POST.get('equipment_name')
        equipment_numbers = int(request.POST.get('equipment_numbers'))
        try:
            equipment = MedicalEquipment.objects.get(name=equipment_name)
            if equipment.numbers > equipment_numbers:
                equipment.numbers -= equipment_numbers
                equipment.save()
                return render(request, 'success.html', {'message': f"Đã giảm {equipment_numbers} thiết bị y tế {equipment_name} khỏi Facility."})
            elif equipment.numbers == equipment_numbers:
                equipment.numbers = 0
                equipment.save()
                return render(request, 'success.html', {'message': f"Đã giảm hết số lượng thiết bị y tế {equipment_name} khỏi Facility."})
            else:
                return render(request, 'error.html', {'message': f"Số lượng thiết bị y tế {equipment_name} trong Facility không đủ."})
        except MedicalEquipment.DoesNotExist:
            return render(request, 'error.html', {'message': f"Không tìm thấy thiết bị y tế có tên {equipment_name}."})
    else:
        return render(request, 'remove_medical_equipment.html')

def medical_equipment_info(request):
    facility = Facility.objects.first()  # Lấy Facility (cần chỉnh sửa nếu có nhiều Facility)
    if facility == None: 
        facility = Facility.objects.create()

    equipment = facility.get_medical_equipments_info()
    return render(request, 'medical_equipment_info.html', {'equipment': equipment})

def edit_medicine(request):
    if request.method == 'POST':
        medicine_name = request.POST.get('medicine_name')
        new_numbers = int(request.POST.get('medicine_numbers'))
        if new_numbers < 0:
            return render(request, 'error.html', {'message': f"Số lượng thuốc không thể nhỏ hơn 0."})
        try:
            medicine = Medicine.objects.get(name=medicine_name)
            old_numbers = medicine.numbers
            if new_numbers == 0:
                medicine.delete()
                MedicineHistory.objects.create(name=medicine.name, numbers=0, changeType='export')
                return render(request, 'success.html', {'message': f"Đã xóa hết thuốc {medicine_name} khỏi Facility."})
            elif new_numbers > old_numbers:
                medicine.numbers = new_numbers
                medicine.save()
                MedicineHistory.objects.create(name=medicine.name, numbers=new_numbers - old_numbers, changeType='import')
                return render(request, 'success.html', {'message': f"Đã tăng số lượng thuốc {medicine_name} lên {new_numbers}."})
            else:
                medicine.numbers = new_numbers
                medicine.save()
                MedicineHistory.objects.create(name=medicine.name, numbers=old_numbers - new_numbers, changeType='export')
                return render(request, 'success.html', {'message': f"Đã giảm số lượng thuốc {medicine_name} xuống {new_numbers}."})
        except Medicine.DoesNotExist:
            return render(request, 'error.html', {'message': f"Không tìm thấy thuốc có tên {medicine_name}."})
    else:
        return render(request, 'edit_medicine.html')

def edit_medical_equipment(request):
    if request.method == 'POST':
        equipment_name = request.POST.get('equipment_name')
        new_numbers = int(request.POST.get('equipment_numbers'))
        if new_numbers < 0:
            return render(request, 'error.html', {'message': f"Số lượng thiết bị y tế không thể nhỏ hơn 0."})
        try:
            equipment = MedicalEquipment.objects.get(name=equipment_name)
            if new_numbers == 0:
                equipment.delete()
                return render(request, 'success.html', {'message': f"Đã xóa hết thiết bị y tế {equipment_name} khỏi Facility."})
            elif new_numbers > equipment.numbers:
                equipment.numbers = new_numbers
                equipment.save()
                return render(request, 'success.html', {'message': f"Đã tăng số lượng thiết bị y tế {equipment_name} lên {new_numbers}."})
            else:
                equipment.numbers = new_numbers
                equipment.save()
                return render(request, 'success.html', {'message': f"Đã giảm số lượng thiết bị y tế {equipment_name} xuống {new_numbers}."})
        except MedicalEquipment.DoesNotExist:
            return render(request, 'error.html', {'message': f"Không tìm thấy thiết bị y tế có tên {equipment_name}."})
    else:
        return render(request, 'edit_medical_equipment.html')

def medicine_history(request):
    history = MedicineHistory.objects.all().order_by('-date')
    return render(request, 'medicine_history.html', {'history': history})