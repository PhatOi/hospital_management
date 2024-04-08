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