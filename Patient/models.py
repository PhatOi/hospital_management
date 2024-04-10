from django.db import models


class PersonalInfo (models.Model):
    Name = models.CharField(max_length = 100)
    Birthday = models.DateField()
    Nationality = models.CharField(max_length = 100)
    Identity = models.CharField(max_length = 100)
    
class TestResult (models.Model):
    test_date = models.DateField() 
    glucose_blood = models.DecimalField(max_digits=8, decimal_places=2)
    cholesterol = models.DecimalField(max_digits=8, decimal_places=2)
    personal_medical_history = models.TextField()
    medications = models.TextField() 
    allergies = models.TextField() 
    
class Patient (models.Model):
    personal_info = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE)
    test_result = models.ForeignKey(TestResult, on_delete=models.CASCADE)
    
        
 
# Create your models here.
