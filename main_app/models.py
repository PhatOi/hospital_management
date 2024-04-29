import datetime
from django.db import models
from django.core.files.storage import default_storage
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.db.models.signals import post_save
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone
# Create your models here.

# extend/override default auth user 
class CustomUser(AbstractUser):
    user_type_data = ((1,"Admin"),(2,"Staff"),(3,"Patient"))
    user_type = models.CharField(default=1, choices=user_type_data, max_length=10)

    def __str__(self):
        return self.last_name + ", " + self.first_name

# admin
class Manager(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class Staff(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete = models.CASCADE)
    birthday = models.DateField(null=True)
    phone = PhoneNumberField(null=False, blank=False, unique=True)
    address = models.TextField() 
    avatar = models.FileField(upload_to='staff_avatar', null=True, blank=True)
    role = models.CharField(max_length=15, choices= [
        ('Bác sĩ', 'Bác sĩ'),
        ('Y tá', 'Y tá'),
        ('Khác', 'Khác'),
    ])
    certificates = models.ManyToManyField('certificate')
    specialize = models.ManyToManyField('TreatmentFacility')
    available = models.BooleanField(null=True)
    def __str__(self):
        return f"{self.admin.last_name} {self.admin.first_name} "
    
class certificate(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class TreatmentFacility(models.Model):
    facility_choices = [
        ('Khoa khám bệnh', 'Khoa khám bệnh'),
        ('Khoa Hồi sức cấp cứu', 'Khoa Hồi sức cấp cứu'),
        ('Khoa Nội tổng hợp', 'Khoa Nội tổng hợp'),
        ('Khoa Nội tim mạch', 'Khoa Nội tim mạch'),
        ('Khoa Nội tiêu hóa', 'Khoa Nội tiêu hóa'),
        ('Khoa Nội cơ - xương - khớp', 'Khoa Nội cơ - xương - khớp'),
        ('Khoa Nội thận - tiết niệu', 'Khoa Nội thận - tiết niệu'),
        ('Khoa Nội tiết', 'Khoa Nội tiết'),
        ('Khoa Dị ứng', 'Khoa Dị ứng'),
        ('Khoa Truyền nhiễm', 'Khoa Truyền nhiễm'),
        ('Khoa Lao', 'Khoa Lao'),
        ('Khoa Da Liễu', 'Khoa Da Liễu'),
        ('Khoa Thần kinh', 'Khoa Thần kinh'),
        ('Khoa Tâm thần', 'Khoa Tâm thần'),
        ('Khoa Nhi', 'Khoa Nhi'),
        ('Khoa Ngoại tổng hợp', 'Khoa Ngoại tổng hợp'),
        ('Khoa Ngoại thần kinh', 'Khoa Ngoại thần kinh'),
        ('Khoa Ngoại lồng ngực', 'Khoa Ngoại lồng ngực'),
        ('Khoa Ngoại tiêu hóa', 'Khoa Ngoại tiêu hóa'),
        ('Khoa Ngoại thận - tiết niệu', 'Khoa Ngoại thận - tiết niệu'),
        ('Khoa Chấn thương chỉnh hình', 'Khoa Chấn thương chỉnh hình'),
        ('Khoa Phẩu thuật gây mê hồi sức', 'Khoa Phẩu thuật gây mê hồi sức'),
        ('Khoa Phụ sản', 'Khoa Phụ sản'),
        ('Khoa Tai - mũi - họng', 'Khoa Tai - mũi - họng'),
        ('Khoa Răng - hàm - mặt', 'Khoa Răng - hàm - mặt'),
        ('Khoa mắt', 'Khoa mắt'),
        ('Khoa Vật lý trị liệu - phục hồi chức năng', 'Khoa Vật lý trị liệu - phục hồi chức năng'),
        ('Khoa Huyến học', 'Khoa Huyến học'),
        ('Khoa Hóa Sinh', 'Khoa Hóa Sinh'),
        ('Khoa Vi sinh', 'Khoa Vi sinh'),
        ('Khoa Chẩn đoán hình ảnh', 'Khoa Chẩn đoán hình ảnh'),
        ('Khoa Thăm dò chức năng', 'Khoa Thăm dò chức năng'),
        ('Khoa Nội soi', 'Khoa Nội soi'),
        ('Khoa Chống nhiễm khuẩn', 'Khoa Chống nhiễm khuẩn'),
        ('Khoa Dược', 'Khoa Dược'),
        ('Khoa Dinh dưỡng', 'Khoa Dinh dưỡng'),
    ]

    name = models.CharField(max_length=255, choices=facility_choices)

    def __str__(self):
        return self.get_name_display()

class FeedbackStaff(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    feedback = models.TextField()
    reply = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class NotificationStaff(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Patient(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    phone_number = PhoneNumberField(null=False, blank=False, unique=True)
    nationality = models.CharField(max_length = 50)
    gender = models.CharField(max_length = 10, choices=[("male", "Nam"), ("female", "Nữ")])
    date_of_birth = models.DateField(null=True)
    address = models.TextField()
    ID1 = models.CharField(max_length = 30)
    medical_record = models.TextField(null=True) # Tiền sử bệnh lý của bệnh nhân
    avatar = models.FileField(upload_to='patient_avatar', null=True, blank=True)

    #Người giám hộ
    name2 = models.CharField(max_length = 100) 
    phone_number2 = PhoneNumberField(null=False, blank=False, unique=True)
    address2 = models.TextField()
    ID2 = models.CharField(max_length = 30)
    relationship = models.CharField (max_length = 30)

    progress = models.CharField(max_length=100,null=True, choices=[
        ('Đang tiếp nhận', 'Đang tiếp nhận'),
        ('Đang chẩn đoán', 'Đang chẩn đoán'),
        ('Đang điều trị', 'Đang điều trị'),
        ('Xuất viện', 'Xuất viện')
    ])
    def __str__(self):
        return f"{self.admin.last_name} {self.admin.first_name} "
    
    
class FeedbackPatient(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    feedback = models.TextField()
    reply = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    RATING_CHOICES = [(i, i) for i in range(1, 6)]
    rating = models.IntegerField(default=0, blank=True, choices=RATING_CHOICES) 
    
    
class TestResult (models.Model):
    patient = models.OneToOneField(Patient, on_delete = models.CASCADE, null=True)
    test_day = models.DateField(null=True)
    height = models.DecimalField(null=True, max_digits = 6, decimal_places= 2)
    weight = models.DecimalField(null=True, max_digits = 6, decimal_places= 2)
    blood_pressure = models.DecimalField(null=True, max_digits = 6, decimal_places= 2)
    heart_rate = models.DecimalField(null=True, max_digits = 6, decimal_places= 2)
    wbc = models.PositiveIntegerField(null=True)
    rbc = models.PositiveIntegerField(null=True)
    hb = models.PositiveIntegerField(null=True)
    hct = models.PositiveIntegerField(null=True)
    plt = models.PositiveIntegerField(null=True)
    lym = models.PositiveIntegerField(null=True)    
    neut = models.PositiveIntegerField(null=True)
    leu = models.PositiveIntegerField(null=True)
    nit = models.DecimalField(null=True, max_digits = 6, decimal_places= 2)
    pro = models.DecimalField(null=True, max_digits = 6, decimal_places= 3)
    ery = models.PositiveIntegerField(null=True)
    glu = models.PositiveIntegerField(null=True)
    conclusion = models.TextField()
    
class MedicalHistory (models.Model):
    patient = models.ForeignKey(Patient, on_delete = models.CASCADE, null=True)
    date = models.DateField()
    diagnosis = models.TextField() # Chẩn đoán của bác sĩ
    prescription = models.TextField(null=True) # Toa thuốc cần dùng
    treatment_num_days = models.PositiveIntegerField(null=True) # số ngày cần điều trị
    medical_department = models.CharField(choices=TreatmentFacility.facility_choices, null=True, max_length=255)

class TreatmentSchedule(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    label = models.CharField(max_length=30, null=True, choices={'Cuộc hẹn': 'Cuộc hẹn', 'Điều trị': 'Điều trị'})
    start_date = models.DateTimeField(null=True)
    duration = models.PositiveIntegerField(null=True)
    end_date = models.DateTimeField(null=True)
    room = models.CharField(max_length=10)
    facility = models.CharField(max_length=255, null=True, choices=TreatmentFacility.facility_choices)   

    def get_progress(self):
        if (timezone.now() > self.end_date):
            return 100
        if (timezone.now() < self.start_date):
            return 0
        
        days_passed = (timezone.now() - self.start_date).days
        progress_percent = round(min((days_passed / self.duration) * 100, 100),2)
        return progress_percent


class Medicine(models.Model):
    name = models.CharField(max_length=200)
    numbers = models.PositiveIntegerField()
    expiry = models.DateField()

class MedicineHistory(models.Model):
    name = models.CharField(max_length=200)
    numbers = models.PositiveIntegerField()
    changeType = models.CharField(max_length=200)
    date = models.DateTimeField(default=timezone.now)

class MedicalEquipment(models.Model):
    name = models.CharField(max_length=200)
    numbers = models.PositiveIntegerField()
    maintenance_history = models.ManyToManyField('MaintenanceEvent')
    available = models.PositiveIntegerField(null=True)


class MaintenanceEvent(models.Model):
    name = models.CharField(null=True, max_length=255)
    date = models.DateField()
    description = models.TextField()
    explain = models.TextField(null=True)
    maintenance_count = models.IntegerField(null=True)

class Facility(models.Model):
    medicines = models.ManyToManyField(Medicine)
    medical_equipments = models.ManyToManyField(MedicalEquipment)

    def add_medicine(self, medicine):
        self.medicines.add(medicine)

    def remove_medicine(self, medicine):
        self.medicines.remove(medicine)

    def get_medicines_info(self):
        return self.medicines.all()

    def add_medical_equipment(self, equipment):
        self.medical_equipments.add(equipment)

    def get_medical_equipments_info(self):
        return self.medical_equipments.all()

    def edit_medicine(self, medicine):
        pass
    
    def edit_medical_equipment(self, equipment):
        pass




@receiver(post_save, sender = CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.user_type == 1:
            # create a row in Admin table
            Manager.objects.create(admin=instance)
        if instance.user_type == 2:
            Staff.objects.create(admin=instance)
        if instance.user_type == 3:
            Patient.objects.create(admin=instance)


@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    if instance.user_type == 1:
        instance.manager.save()
    if instance.user_type == 2:
        instance.staff.save()
    if instance.user_type == 3:
        instance.patient.save()

