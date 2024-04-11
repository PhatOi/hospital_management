from django.db import models
from django.contrib.auth.models import User


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
    
        
 
# Create your models here.
