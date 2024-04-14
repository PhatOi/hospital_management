from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Profile (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key= True)
    full_name = models.CharField (max_length = 100)
    phone_number = models.CharField(max_length = 20)
    nationality = models.CharField(max_length = 50)
    gender = models.CharField(max_length = 10)
    date_of_birth = models.DateField()
    address = models.CharField (max_length = 100)
    ID1 = models.CharField(max_length = 30)
    #avatar = models.ImageField(upload_to='profile_pics/')
    #Người giám hộ
    name2 = models.CharField(max_length = 100) 
    phone_number2 = models.CharField(max_length = 20)
    address2 = models.CharField (max_length = 100)
    ID2 = models.CharField(max_length = 30)
    relationship = models.CharField (max_length = 30)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    def __str__(self):
        return self.full_name
    
    
class Feedback (models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    description = models.TextField()
    time = models.DateTimeField(default=timezone.now)
    RATING_CHOICES = [(i, i) for i in range(1, 6)]  # Danh sách chứa tuples từ 1 đến 
    rating = models.IntegerField(choices=RATING_CHOICES) 
    def __str__(self):
        return self.full_name
    
    
class TestResult (models.Model):
    patient = models.OneToOneField(User, on_delete = models.CASCADE)
    height = models.DecimalField(max_digits = 6, decimal_places= 2)
    weight = models.DecimalField(max_digits = 6, decimal_places= 2)
    blood_pressure = models.DecimalField(max_digits = 6, decimal_places= 2)
    heart_rate = models.DecimalField(max_digits = 6, decimal_places= 2)
    blood_test = models.CharField(max_length = 100)
    urinalysis = models.CharField(max_length = 100)
    conclusion = models.TextField()
    
class MedicalDate (models.Model):
    patient = models.ForeignKey(User, on_delete = models.CASCADE)
    date = models.DateField()
    description = models.TextField()
# Create your models here.
