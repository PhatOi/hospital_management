from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import *

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

def maintenanceEquip(request):
    equipment_name = request.POST.get('equipment_name')
    maintenance_count = int(request.POST.get('maintenance_count'))

    equipment = facility.medical_equipments.get(name=equipment_name)

    if maintenance_count > equipment.available:
        return render(request, 'edit_medical_equipment.html', {'error_message': 'Số lượng bảo dưỡng không thể lớn hơn số lượng thiết bị hiện có.'})

    if maintenance_count < 0:
        return render(request, 'edit_medical_equipment.html', {'error_message': 'Số lượng bảo dưỡng không thể là số âm.'})

    equipment.available -= maintenance_count
    equipment.save()

    maintenance_event = MaintenanceEvent.objects.create(
        name=f'Bảo dưỡng {equipment.name}',
            date=datetime.date.today(),
            description=f'Bảo dưỡng {maintenance_count} {equipment.name}.',
            maintenance_count=maintenance_count,
    )

    # Thêm sự kiện bảo dưỡng vào lịch sử bảo dưỡng của thiết bị
    equipment.maintenance_history.add(maintenance_event)

    return render(request, 'edit_medical_equipment.html', {'success_message': f'Bảo dưỡng {equipment.name} thành công.'})

def maintenanceHistory(request):
    history = MaintenanceEvent.objects.all().order_by('-date')
    return render(request, 'maintenance_history.html', {'history': history})