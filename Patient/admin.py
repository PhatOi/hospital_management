from django.contrib import admin


from .models import Profile, Feedback, MedicalDate, TestResult

admin.site.register(Feedback)
admin.site.register(Profile)
admin.site.register(MedicalDate)
admin.site.register(TestResult)
# Register your models here.
