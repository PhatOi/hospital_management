from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Thêm các trường thông tin bổ sung tại đây nếu cần



# Create your models here.
