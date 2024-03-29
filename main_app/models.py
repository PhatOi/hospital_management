from django.db import models
from django.contrib.auth.models import User

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
    objects = models.Manager()

class Staff(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.IntegerField()
    Phone = models.IntegerField()
    Address = models.TextField() 
    Avatar = models.FileField()
    Role = models.CharField()
    Certificate = models.CharField()
    Specialize = models.CharField()
    Availablle = models.BooleanField()