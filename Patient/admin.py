from django.contrib import admin


from .models import Profile, Feedback, MedicalDate 

admin.site.register(Feedback)
admin.site.register(Profile)
admin.site.register(MedicalDate)
# Register your models here.
