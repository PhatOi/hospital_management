from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Thêm các trường thông tin bổ sung tại đây nếu cần



# Create your models here.

class Admin(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    # objects = models.Manager()
    def __str__(self):
        return f"{self.name}"

class Staff(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.IntegerField()
    Phone = models.CharField(max_length=15)
    Address = models.TextField() 
    Avatar = models.FileField()
    Role = models.CharField(max_length=15)
    Certificate = models.CharField(max_length=255)
    Specialize = models.JSONField(max_length=255)
    Availablle = models.BooleanField()
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

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
    available = models.BooleanField(default=True)

class MaintenanceEvent(models.Model):
    date = models.DateField()
    description = models.TextField()

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
    
    def medicine_history(self):
        pass