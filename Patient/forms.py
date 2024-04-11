from django import forms 
from .models import Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 


        
class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User 
        fields = ['username', 'email', 'password1', 'password2']
        
        
class PatientProfileForm(forms.ModelForm):
    class Meta:
        model = Profile 
        fields = ['user','full_name', 'phone_number', 'nationality', 'gender', 'date_of_birth', 'address', 'ID1', 'name2', 'phone_number2', 'address2', 'ID2', 'relationship', 'avatar']
        labels = {
            'full_name': 'Họ và tên',
            'phone_number': 'Số điện thoại',
            'nationality': 'Quốc tịch',
            'gender': 'Giới tính',
            'date_of_birth': 'Ngày sinh',
            'address': 'Địa chỉ',
            'ID1': 'Căn cước công dân/chứng minh nhân dân',
            'avatar': 'Ảnh đại diện',
            'name2': 'Tên người thân',
            'phone_number2': 'Số điện thoại người thân',
            'address2': 'Địa chỉ người thân',
            'ID2': 'Căn cước công dân/chứng minh nhân dân người thân',
            'relationship': 'Mối quan hệ với người thân',
            
        }
    