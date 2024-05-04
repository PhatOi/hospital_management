from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.views.decorators.csrf import csrf_exempt
from django.utils.timezone import localtime
from django.db.models import Count
from django.db.models.functions import ExtractMonth
from datetime import datetime, timedelta
from main_app.models import CustomUser
import datetime
import json
from .models import *
from .form import *



def admin_home(request):
    total_medicine = 0
    medicines = Medicine.objects.all()
    for medicine in medicines:
        total_medicine += medicine.numbers

    total_equipment = 0
    equipments = MedicalEquipment.objects.all()
    for equipment in equipments:
        total_equipment += equipment.numbers

    staff_role = ['Bác sĩ', 'Y tá', 'Khác']
    staff_role_count = [Staff.objects.filter(role='Bác sĩ').count(), Staff.objects.filter(role='Y tá').count(), Staff.objects.filter(role='Khác').count()]
    total_staff = sum(staff_role_count)

    status_label = ['Đang tiếp nhận', 'Đang chẩn đoán', 'Đang điều trị', 'Xuất viện']
    status_label_count = [Patient.objects.filter(progress='Đang tiếp nhận').count(), Patient.objects.filter(progress='Đang chẩn đoán').count(), Patient.objects.filter(progress='Đang điều trị').count(), Patient.objects.filter(progress='Xuất viện').count()]
    total_patient = sum(status_label_count)

    patient_join_count = CustomUser.objects.filter(user_type=3).annotate(month=ExtractMonth('date_joined')).values('month').annotate(count=Count('id')).order_by('month')
    month_join_label = []
    month_join_number = []
    for month in patient_join_count:
        month_join_label.append(month['month'])
        month_join_number.append(month['count']) 

    # Tổng feedback 1->5
    patient_feedbacks = FeedbackPatient.objects.all()
    rate_label = ['1', '2', '3', '4', '5']
    rate_label_count = [0, 0, 0, 0, 0]
    for patient_feedback in patient_feedbacks:
        if patient_feedback.rating == 0:
            continue
        rate_label_count[patient_feedback.rating - 1] += 1

    context = {
        'total_staff': total_staff,
        'total_patient': total_patient,
        'total_medicine': total_medicine,
        'total_equipment': total_equipment,
        'staff_role': staff_role,
        'staff_role_count': staff_role_count,
        'status_label': status_label,
        'status_label_count': status_label_count,
        'month_join_label': month_join_label,
        'month_join_number': month_join_number,
        'rate_label': rate_label,
        'rate_label_count': rate_label_count,
    }    

    return render(request, 'admin_template/home.html', context)


def add_staff(request):
    form = StaffForm(request.POST or None, request.FILES or None)
    if request.method == "POST":
        if form.is_valid():
            first_name = form.cleaned_data.get("first_name") 
            last_name = form.cleaned_data.get("last_name")
            email = form.cleaned_data.get("email") 
            password = form.cleaned_data.get("password")
            birthday = form.cleaned_data.get("birthday") 
            phone = form.cleaned_data.get("phone") 
            address = form.cleaned_data.get("address") 
            avatar = form.cleaned_data["avatar"]
            role = form.cleaned_data.get("role") 
            certificates = [form.cleaned_data.get("certificate")]
            cs = request.POST.getlist('certificate')
            if len(cs) > 1:
                certificates = [i.strip() for i in cs]

            specialize = form.cleaned_data.get("specialize") 
            available = form.cleaned_data.get("available")      

            try:
                user=CustomUser.objects.create_user(username= email,email=email, password=password, first_name=first_name,last_name=last_name, user_type=2)
                user.staff.birthday = birthday
                user.staff.phone = phone
                user.staff.address = address 
                user.staff.avatar = avatar 
                user.staff.role = role
                user.staff.available = available
                for c in certificates:
                    if not c:
                        raise ValidationError("Không được để trống")
                    else:
                        certificate_obj, created = certificate.objects.get_or_create(name=c)
                        user.staff.certificates.add(certificate_obj)
                
                for s in specialize:
                    treatmentfacility_obj, created = TreatmentFacility.objects.get_or_create(name=s)
                    user.staff.specialize.add(treatmentfacility_obj)
                
                user.save()
                messages.success(request, "Thêm nhân viên thành công")
                return HttpResponseRedirect(reverse("add_staff"))
            except:
                messages.error(request, "Thêm nhân viên thất bại")
                return HttpResponseRedirect(reverse("add_staff"))
        else:
            messages.error(request, "Hãy đáp ứng mọi yêu cầu")


    return render(request, "admin_template/add_staff.html", {'form': form})


def manage_staff(request):
    update_staff_availability()
    staffs = Staff.objects.order_by('id')
    return render(request, "admin_template/manage_staff.html", {'staffs': staffs})


def edit_staff(request, staff_id):
    staff = Staff.objects.get(admin=staff_id)
    form = StaffForm(request.POST or None, request.FILES or None, instance=staff)

    if request.method == "POST":
        if form.is_valid():
            certificates = [form.cleaned_data.get("certificate")]
            cs = request.POST.getlist('certificate')
            if len(cs) > 1:
                certificates = [i.strip() for i in cs]

            specialize = form.cleaned_data.get("specialize")      
            try:
                user = CustomUser.objects.get(id=staff.admin.id)
                user.first_name = form.cleaned_data.get("first_name") 
                user.last_name = form.cleaned_data.get("last_name")
                user.email = form.cleaned_data.get("email") 
                password = form.cleaned_data.get("password") or None
                if password != None:
                    user.set_password(password)                
                staff.birthday = form.cleaned_data.get("birthday") 
                staff.phone = form.cleaned_data.get("phone") 
                staff.address = form.cleaned_data.get("address") 
                avatar = form.cleaned_data["avatar"]
                if avatar:
                    staff.avatar = form.cleaned_data["avatar"]
                else:
                    staff.avatar = None
                staff.role = form.cleaned_data.get("role") 
                staff.available = form.cleaned_data.get("available")

                # handle certificates 
                old_certificates = set(staff.certificates.values_list('name', flat=True))
                certificates = set(certificates)
                # new certificates
                certificates_to_add = certificates - old_certificates
                for c in certificates_to_add:
                    if not c:
                        raise ValidationError("Không được để trống")
                    else:
                        certificate_obj, created = certificate.objects.get_or_create(name=c)
                        staff.certificates.add(certificate_obj)

                # remove old certificates not in new list
                certificates_to_remove = old_certificates - certificates
                for c in certificates_to_remove:
                    certificate_obj = certificate.objects.get(name=c)
                    staff.certificates.remove(certificate_obj)                

                # handle specialize
                old_specialize = set(staff.specialize.values_list('name', flat=True))
                specialize = set(specialize)
                # new specialize
                specializes_to_add = specialize - old_specialize
                for c in specializes_to_add:
                    try:
                        specialize_obj, created = TreatmentFacility.objects.get_or_create(name=c)
                        staff.specialize.add(specialize_obj)
                    except Exception as e:
                        print(e)
                        
                # remove old specialize not in new list
                specialize_to_remove = old_specialize - specialize
                for c in specialize_to_remove:
                    specialize_obj = TreatmentFacility.objects.get(name=c)
                    staff.specialize.remove(specialize_obj)                

                user.save()
                staff.save()
                messages.success(request, "Cập nhật thành công")
                return HttpResponseRedirect(reverse("edit_staff", kwargs={'staff_id': staff_id}))
            except:
                messages.error(request, "Câp nhật thất bại")
                return HttpResponseRedirect(reverse("edit_staff", kwargs={'staff_id': staff_id}))
        else:
            messages.error(request, "Hãy đáp ứng mọi yêu cầu")
            
    return render(request,"admin_template/edit_staff.html", {'staff': staff, 'form': form})


def delete_staff(request, staff_id):
    staff = get_object_or_404(CustomUser, id=staff_id)
    staff.delete()
    messages.success(request, "Đã xóa nhân viên thành công!")    
    return HttpResponseRedirect(reverse("manage_all_staff"))


def add_patient(request):
    form = PatientForm(request.POST or None, request.FILES or None)
    if request.method == "POST":
        if form.is_valid():
            first_name = form.cleaned_data.get("first_name") 
            last_name = form.cleaned_data.get("last_name")
            email = form.cleaned_data.get("email") 
            password = form.cleaned_data.get("password")
            try:
                user=CustomUser.objects.create_user(username=email,email=email, password=password, first_name=first_name,last_name=last_name, user_type=3)
                user.patient.phone_number = form.cleaned_data.get("phone_number") 
                user.patient.nationality = form.cleaned_data.get("nationality") 
                user.patient.gender = form.cleaned_data.get("gender")
                user.patient.date_of_birth = form.cleaned_data.get("date_of_birth")
                user.patient.address = form.cleaned_data.get("address")
                user.patient.ID1 = form.cleaned_data.get("ID1")
                user.patient.avatar = form.cleaned_data["avatar"]
                user.patient.medical_record = form.cleaned_data.get("medical_record")
                user.patient.name2 = form.cleaned_data.get("name2")
                user.patient.phone_number2 = form.cleaned_data.get("phone_number2")
                user.patient.address2 = form.cleaned_data.get("address2")
                user.patient.ID2 = form.cleaned_data.get("ID2")
                user.patient.relationship = form.cleaned_data.get("relationship") 
                user.patient.progress = form.cleaned_data.get("progress")
                user.save()
                TestResult.objects.get_or_create(patient=user.patient)
                messages.success(request, "Thêm bệnh nhân thành công")
                return HttpResponseRedirect(reverse("add_patient"))
            except:
                messages.error(request, "Thêm bệnh nhân thất bại")
                return HttpResponseRedirect(reverse("add_patient"))
        else:
            messages.error(request, "Hãy đáp ứng mọi yêu cầu")


    return render(request, "admin_template/add_patient.html", {'form': form})


def manage_patient(request):
    patients = Patient.objects.order_by('id')
    patients_progress = []

    for patient in patients:
        schedules = TreatmentSchedule.objects.filter(patient=patient)
        if any(schedules):
            schedule = schedules.latest('start_date')
            progress_percent = schedule.get_progress() 
        else:
            progress_percent = 0

        patients_progress.append((patient, progress_percent))

    return render(request, "admin_template/manage_patient.html", {'patients': patients_progress})


def edit_patient(request, patient_id):
    patient = Patient.objects.get(admin=patient_id)
    form = PatientForm(request.POST or None, request.FILES or None, instance=patient)
    if request.method == "POST":
        if form.is_valid():
            try:
                user = CustomUser.objects.get(id=patient.admin.id)
                user.first_name = form.cleaned_data.get("first_name") 
                user.last_name = form.cleaned_data.get("last_name")
                user.email = form.cleaned_data.get("email") 
                password = form.cleaned_data.get("password") or None
                if password != None:
                    user.set_password(password)   
                       
                user.save()
                form.save()
                messages.success(request, "Cập nhật thành công")
                return HttpResponseRedirect(reverse("edit_patient", kwargs={'patient_id': patient_id}))
            except:
                messages.error(request, "Cập nhật thất bại")
                return HttpResponseRedirect(reverse("edit_patient", kwargs={'patient_id': patient_id}))
        else:
            messages.error(request, "Hãy đáp ứng mọi yêu cầu")
            
    return render(request,"admin_template/edit_patient.html", {'patient': patient, 'form': form})    


def test_result(request, patient_id):
    test_result, created = TestResult.objects.get_or_create(patient_id=patient_id) 
    form = TestResultForm(request.POST or None, request.FILES or None, instance=test_result)
    if request.method == "POST":
        if form.is_valid():
            try:
                form.save()
                messages.success(request, "Lưu kết quả thành công")
                return HttpResponseRedirect(reverse("test_result", kwargs={'patient_id': patient_id}))
            except:
                messages.error(request, "Lưu kết quả không thành công")
                return HttpResponseRedirect(reverse("test_result", kwargs={'patient_id': patient_id}))
        else:
            messages.error(request, "Hãy đáp ứng mọi yêu cầu")
            
    return render(request,"admin_template/test_result.html", {'test_result': test_result, 'form': form}) 


def medical_history(request, patient_id):
    patient = get_object_or_404(Patient, pk=patient_id)
    history = MedicalHistory.objects.filter(patient=patient).order_by('-date')
    form = MedicalHistoryForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            try:
                medical_history = form.save(commit=False)
                medical_history.patient = patient
                medical_history.save()
                messages.success(request, "Lưu bệnh án thành công")
                return HttpResponseRedirect(reverse("medical_history", kwargs={'patient_id': patient_id}))
            except:
                messages.error(request, "Lưu bệnh án không thành công")
                return HttpResponseRedirect(reverse("medical_history", kwargs={'patient_id': patient_id}))
        else:
            messages.error(request, "Hãy đáp ứng mọi yêu cầu")
    return render(request, 'admin_template/medical_history.html', {'patient': patient, 'history': history, 'form': form})


def delete_patient(request, patient_id):
    patient = get_object_or_404(CustomUser, id=patient_id)
    patient.delete()
    messages.success(request, "Đã xóa bệnh nhân thành công!")    
    return HttpResponseRedirect(reverse("manage_all_patient"))


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
            MedicineHistory.objects.create(name=medicine.name, numbers=medicine_numbers, changeType='Nhập kho')
            messages.success(request, f"Đã thêm {medicine_numbers} thuốc {medicine_name} vào kho.")
            return HttpResponseRedirect(reverse("add_medicine"))
        except Medicine.DoesNotExist:
            new_medicine = Medicine.objects.create(name=medicine_name, numbers=medicine_numbers, expiry=medicine_expiry)
            facility.add_medicine(new_medicine)
            MedicineHistory.objects.create(name=new_medicine.name, numbers=new_medicine.numbers, changeType='Nhập kho')
            messages.success(request, f"Đã thêm thuốc mới {medicine_name} vào kho.")
            return HttpResponseRedirect(reverse("add_medicine"))           
    else:
        return render(request, 'admin_template/add_medicine.html')


def remove_medicine(request, medicine_id):
    medicine = get_object_or_404(Medicine, id=medicine_id)
    medicine_name = medicine.name
    MedicineHistory.objects.create(name=medicine.name, numbers=medicine.numbers, changeType='Xuất kho')
    medicine.delete()
    messages.success(request, f"Đã xóa thuốc {medicine_name} thành công!")    
    return HttpResponseRedirect(reverse("manage_medicine"))


def manage_medicine(request):
    facility = Facility.objects.first()  # Lấy Facility (cần chỉnh sửa nếu có nhiều Facility)
    if facility == None: 
        facility = Facility.objects.create()

    medicines = facility.get_medicines_info()
    return render(request, 'admin_template/manage_medicine.html', {'medicines': medicines})


def medicine_history(request):
    history = MedicineHistory.objects.all().order_by('-date')
    return render(request, 'admin_template/medicine_history.html', {'history': history})


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
            equipment.available += equipment_numbers
            equipment.save()
            messages.success(request, f"Đã thêm {equipment_numbers} thiết bị y tế {equipment_name} vào kho.")
            return HttpResponseRedirect(reverse('add_medical_equipment'))

        except MedicalEquipment.DoesNotExist:
            new_equipment = MedicalEquipment.objects.create(name=equipment_name, numbers=equipment_numbers,available=equipment_numbers)
            facility.add_medical_equipment(new_equipment)
            messages.success(request, f"Đã thêm thiết bị y tế mới {equipment_name} vào kho.")
            return HttpResponseRedirect(reverse('add_medical_equipment'))
    else:
        return render(request, 'admin_template/add_medical_equipment.html')


def remove_medical_equipment(request, equip_id):
    equip = get_object_or_404(MedicalEquipment, id=equip_id)
    equip_name = equip.name
    equip.delete()
    messages.success(request, f"Đã xóa thiết bị {equip_name} thành công!")    
    return HttpResponseRedirect(reverse("manage_equip"))


def manage_equip(request):
    facility = Facility.objects.first()  # Lấy Facility (cần chỉnh sửa nếu có nhiều Facility)
    if facility == None: 
        facility = Facility.objects.create()

    equipment = facility.get_medical_equipments_info()
    return render(request, 'admin_template/manage_equip.html', {'equipment': equipment})


def edit_medicine(request, medicine_id):
    medicine = Medicine.objects.get(id=medicine_id)
    if request.method == 'POST':
        medicine_name = request.POST.get('medicine_name')
        new_numbers = int(request.POST.get('medicine_numbers'))
        medicine_expiry = request.POST.get('medicine_expiry')
        if new_numbers < 0:
            messages.error(request, f"Số lượng thuốc không thể nhỏ hơn 0.")
            return HttpResponseRedirect(reverse("edit_medicine", kwargs={'medicine_id': medicine_id}))
        try:
            medicine = Medicine.objects.get(name=medicine_name)
            medicine.expiry = medicine_expiry        
            old_numbers = medicine.numbers
            medicine.numbers = new_numbers
            medicine.save()
            if new_numbers == 0:
                MedicineHistory.objects.create(name=medicine.name, numbers=old_numbers, changeType='Xuất kho')
                messages.success(request, f"Đã xóa hết thuốc {medicine_name} khỏi kho.")
                return HttpResponseRedirect(reverse("edit_medicine", kwargs={'medicine_id': medicine_id}))
            elif new_numbers > old_numbers:
                MedicineHistory.objects.create(name=medicine.name, numbers=new_numbers - old_numbers, changeType='Nhập kho')
                messages.success(request, f"Đã tăng số lượng thuốc {medicine_name} lên {new_numbers}.")
                return HttpResponseRedirect(reverse("edit_medicine", kwargs={'medicine_id': medicine_id}))
            else:
                MedicineHistory.objects.create(name=medicine.name, numbers=old_numbers - new_numbers, changeType='Xuất kho')
                messages.success(request, f"Đã giảm số lượng thuốc {medicine_name} xuống {new_numbers}.")
                return HttpResponseRedirect(reverse("edit_medicine", kwargs={'medicine_id': medicine_id}))
        except Medicine.DoesNotExist:
            messages.error(request, f"Không tìm thấy thuốc có tên {medicine_name}.")
            return HttpResponseRedirect(reverse("edit_medicine", kwargs={'medicine_id': medicine_id}))
    else:
        return render(request, 'admin_template/edit_medicine.html', {'medicine': medicine})


def edit_medical_equipment(request, equip_id):
    equip = MedicalEquipment.objects.get(id=equip_id)
    if request.method == 'POST':
        equipment_name = request.POST.get('equipment_name')
        new_available = int(request.POST.get('equipment_available'))
        if new_available < 0:
            messages.error(request, f"Số lượng thiết bị y tế không thể nhỏ hơn 0.")
            return HttpResponseRedirect(reverse("edit_medical_equipment", kwargs={'equip_id': equip_id}))
        try:
            equipment = MedicalEquipment.objects.get(name=equipment_name)
            if new_available == 0:
                equipment.numbers = 0
                equipment.available = 0
                equipment.save()
                messages.success(request, f"Đã xóa hết thiết bị y tế {equipment_name} khỏi kho.")
                return HttpResponseRedirect(reverse("edit_medical_equipment", kwargs={'equip_id': equip_id}))
            elif new_available > equipment.available:
                equipment.numbers += (new_available - equipment.available)
                equipment.available = new_available
                equipment.save()
                messages.success(request, f"Đã tăng số lượng thiết bị y tế {equipment_name} lên {new_available}.")
                return HttpResponseRedirect(reverse("edit_medical_equipment", kwargs={'equip_id': equip_id}))
            else:
                equipment.numbers -= (equipment.available - new_available)
                equipment.available = new_available
                equipment.save()
                messages.success(request, f"Đã giảm số lượng thiết bị y tế {equipment_name} xuống {new_available}.")
                return HttpResponseRedirect(reverse("edit_medical_equipment", kwargs={'equip_id': equip_id}))
        except MedicalEquipment.DoesNotExist:
            messages.error(request, f"Không tìm thấy thiết bị y tế có tên {equipment_name}.")
            return HttpResponseRedirect(reverse("edit_medical_equipment", kwargs={'equip_id': equip_id}))
    else:
        return render(request, 'admin_template/edit_medical_equipment.html', {'equip': equip})


def maintain_equip(request, equip_id):
    equip = MedicalEquipment.objects.get(id=equip_id)
    old_maintenance_count = equip.numbers - equip.available
    if request.method == "POST":
        equipment_name = request.POST.get('equipment_name')
        new_maintenance_count = int(request.POST.get('maintenance_count'))
        explain = request.POST.get('explain')
        try:
            equipment = MedicalEquipment.objects.get(name=equipment_name)

            if (new_maintenance_count > old_maintenance_count and (new_maintenance_count - old_maintenance_count) > equipment.available) or new_maintenance_count < 0:
                messages.error(request, 'Số lượng bảo dưỡng không thể lớn hơn số lượng thiết bị hiện có hoặc là số âm.')
                return HttpResponseRedirect(reverse("maintain_equip", kwargs={'equip_id': equip_id}))

            if new_maintenance_count > old_maintenance_count:
                equipment.available -= (new_maintenance_count - old_maintenance_count)
                equipment.save()
                maintenance_event = MaintenanceEvent.objects.create(
                    name = equipment.name,
                    date = datetime.date.today(),
                    description = f'Bảo dưỡng thêm {new_maintenance_count - old_maintenance_count} {equipment.name}.',
                    maintenance_count= new_maintenance_count - old_maintenance_count,
                    explain = explain
                )
                equipment.maintenance_history.add(maintenance_event)
            elif new_maintenance_count < old_maintenance_count:
                equipment.available += (old_maintenance_count - new_maintenance_count)
                equipment.save()
                maintenance_event = MaintenanceEvent.objects.create(
                    name= equipment.name,
                    date=datetime.date.today(),
                    description=f'Đã bảo dưỡng xong {old_maintenance_count - new_maintenance_count} {equipment.name}.',
                    maintenance_count=old_maintenance_count - new_maintenance_count,
                    explain = explain   
                )
                equipment.maintenance_history.add(maintenance_event)

            messages.success(request, f'Bảo dưỡng {equipment.name} thành công.')
            return HttpResponseRedirect(reverse("maintain_equip", kwargs={'equip_id': equip_id}))
        except MedicalEquipment.DoesNotExist:
            messages.error(request, f"Không tìm thấy thiết bị y tế có tên {equipment_name}.")
            return HttpResponseRedirect(reverse("maintain_equip", kwargs={'equip_id': equip_id}))
    else:
        return render(request, 'admin_template/maintain_equip.html', {'equip': equip, 'n_maintain': old_maintenance_count})


def maintenance_history(request):
    history = MaintenanceEvent.objects.all().order_by('-date')
    return render(request, 'admin_template/maintenance_history.html', {'history': history})


def staff_feedback(request):
    if request.method != 'POST':
        feedbacks = FeedbackStaff.objects.all()
        return render(request, 'admin_template/staff_feedback.html', {'feedbacks': feedbacks})
    else:
        feedback_id = request.POST.get('id')
        try:
            feedback = get_object_or_404(FeedbackStaff, id=feedback_id)
            reply = request.POST.get('reply_message')
            feedback.reply = reply
            feedback.save()
            messages.success(request,"Phản hồi đã được gửi")
            return HttpResponseRedirect(reverse('staff_all_feedback'))
        except:
            messages.error(request,"Gửi phản hồi không thành công")
            return HttpResponseRedirect(reverse('staff_all_feedback'))


def patient_feedback(request):
    if request.method != 'POST':
        feedbacks = FeedbackPatient.objects.all()
        return render(request, 'admin_template/patient_feedback.html', {'feedbacks': feedbacks})
    else:
        feedback_id = request.POST.get('id')
        try:
            feedback = get_object_or_404(FeedbackPatient, id=feedback_id)
            reply = request.POST.get('reply_message')
            feedback.reply = reply + "- Từ quản lý bệnh viện"
            feedback.save()
            messages.success(request,"Phản hồi đã được gửi")
            return HttpResponseRedirect(reverse('patient_all_feedback'))
        except:
            messages.error(request,"Gửi phản hồi không thành công")
            return HttpResponseRedirect(reverse('patient_all_feedback'))


def add_event(request):
    form = TreatmentScheduleForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            try:
                start_date = form.cleaned_data['start_date']
                my_timezone = timezone.get_current_timezone()  
                end_date = form.cleaned_data['end_date']  
                start_date = start_date.astimezone(my_timezone)
                end_date = end_date.astimezone(my_timezone)

                event = form.save(commit=False)
                event.staff = get_object_or_404(Staff, pk = request.POST.get('staff')) 

                event.staff.available = False
                event.duration = request.POST.get('id_duration')
                event.staff.save()
                event.save()
                messages.success(request, "Tạo sự kiện thành công")
                return HttpResponseRedirect(reverse('work_schedules'))
            except:
                messages.error(request, "Tạo sự kiện không thành công")
                return HttpResponseRedirect(reverse('work_schedules'))
        else:
            messages.error(request, "Hãy đáp ứng mọi yêu cầu")

    return HttpResponseRedirect(reverse('work_schedules'))

def delete_event(request, event_id):
    event = TreatmentSchedule.objects.get(id=event_id)
    event.staff.available = True
    event.staff.save()
    event.delete()
    messages.success(request, "Xóa sự kiện thành công")
    return HttpResponseRedirect(reverse('work_schedules'))

def edit_event(request):
    old_event = TreatmentSchedule.objects.get(id=request.POST.get('event_id'))
    form = TreatmentScheduleForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            try:
                start_date = form.cleaned_data['start_date']
                my_timezone = timezone.get_current_timezone()  
                end_date = form.cleaned_data['end_date']  
                start_date = start_date.astimezone(my_timezone)
                end_date = end_date.astimezone(my_timezone)

                new_event = form.save(commit=False)
                
                new_staff = get_object_or_404(Staff, pk = request.POST.get('staff'))
                if old_event.staff != None and old_event.staff != new_staff:
                    old_event_staff = TreatmentSchedule.objects.filter(staff=old_event.staff)
                    if (any(old_event_staff) and old_event_staff.latest('start_date').start_date >= timezone.now() and old_event_staff.latest() != old_event):
                        pass
                    else: 
                        old_event.staff.available = True
                        
                    old_event.staff.save()
                
                new_event.staff = new_staff


                try:
                    old_event.delete()
                except:
                    pass
                
                new_event.staff.available = False
                new_event.duration = request.POST.get('id_duration')
                new_event.staff.save()
                new_event.save()
                messages.success(request, "Cập nhật thành công")
                return HttpResponseRedirect(reverse('work_schedules'))
            except:
                messages.error(request, "Cập nhật không thành công")
                return HttpResponseRedirect(reverse('work_schedules'))
        else:
            messages.error(request, "Hãy đáp ứng mọi yêu cầu")

    return HttpResponseRedirect(reverse('work_schedules'))    

def work_schedules(request):
    form = TreatmentScheduleForm(request.POST or None, request.FILES or None)
    events = TreatmentSchedule.objects.all().order_by('start_date')

    # collect all event by days
    event_dict = {}
    for event in events:
        
        current_date = event.start_date.date()
        if (event.end_date.date() - current_date) <= timedelta(days=1) and event.label == 'Cuộc hẹn':
            if current_date not in event_dict:
                event_dict[current_date] = []
            event_dict[current_date].append(event)
            continue   

        while current_date <= event.end_date.date():
            if current_date not in event_dict:
                event_dict[current_date] = []
            event_dict[current_date].append(event)
            current_date += timedelta(days=1)

    event_dict = dict(sorted(event_dict.items()))

    return render(request, 'admin_template/works.html', {'form': form, 'event_dict': event_dict})

def update_staff_availability():
    now = timezone.now()
    staffs = Staff.objects.all()

    for staff in staffs:
        schedules = TreatmentSchedule.objects.filter(staff=staff)
        # update staff available based on schedules 
        staff.available = not any(schedule.start_date <= now <= schedule.end_date for schedule in schedules)
        staff.save()


def staff_of_facilities(request, facility_id):
    staff = Staff.objects.filter(specialize=facility_id, available=True)
    staff_names = [(s.id, str(s)) for s in staff]
    return JsonResponse(staff_names, safe=False)

def patient_medical_info(request, patient_id):    
    patient = get_object_or_404(Patient, pk=patient_id)
    medical_history = MedicalHistory.objects.filter(patient=patient)
    if any(medical_history):
        m = medical_history.latest('date')
        medical_info = (m.treatment_num_days, m.medical_department)
        return JsonResponse(medical_info, safe=False)
    return JsonResponse("False", safe=False)

@csrf_exempt
def check_staff_available(request):
    body = json.loads(request.body)
    my_timezone = timezone.get_current_timezone()
    start_date = datetime.datetime.strptime(body['startDate'], '%Y-%m-%dT%H:%M')
    end_date = datetime.datetime.strptime(body['endDate'], '%Y-%m-%dT%H:%M')
    start_date = start_date.astimezone(my_timezone)
    end_date = end_date.astimezone(my_timezone)
    facility_name = body['facility']

    staff_names = []
    staffs = Staff.objects.filter(specialize=facility_name)
    for staff in staffs:
        overlap_schedules = TreatmentSchedule.objects.filter(
            staff=staff,
            start_date__lt=end_date,
            end_date__gt=start_date
        )
        if not overlap_schedules.exists():
            staff_names.append((staff.id, str(staff)))

    return JsonResponse(staff_names, safe=False)


@csrf_exempt
def check_email_exist(request):
    body = json.loads(request.body)

    user = CustomUser.objects.filter(email=body['email']).exists()
    if user:
        return JsonResponse("True", safe=False)
    
    return JsonResponse("False", safe=False)

def admin_profile(request):
    user =  get_object_or_404(Manager, admin=request.user)
    form = AdminForm(request.POST or None, request.FILES or None, instance=user)
    if request.method == 'POST':
        if form.is_valid():
            try:
                admin_user = CustomUser.objects.get(id=request.user.id)
                admin_user.first_name = form.cleaned_data.get("first_name") 
                admin_user.last_name = form.cleaned_data.get("last_name")
                admin_user.email = form.cleaned_data.get("email") 
                password = form.cleaned_data.get("password") or None
                if password != None:
                    admin_user.set_password(password)   
                        
                admin_user.save()
                form.save()
                messages.success(request, 'Cập nhật thành công')
                return HttpResponseRedirect(reverse('admin_profile'))
            except:
                messages.error(request, 'Cập nhật thất bại')
                return HttpResponseRedirect(reverse('admin_profile'))
        else:
            messages.error(request, "Hãy đáp ứng mọi yêu cầu")
        
    return render(request, 'admin_template/admin_profile.html', {'form': form})