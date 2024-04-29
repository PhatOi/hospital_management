from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
# Register your models here.


# encript password
class UserModel(UserAdmin):
    pass 

# register custom user model
admin.site.register(CustomUser, UserModel)
