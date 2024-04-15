from django import forms 
from .models import Profile, Feedback
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
        fields = ['full_name', 'phone_number', 'nationality', 'gender', 'date_of_birth', 'address', 'medical_record', 'ID1', 'name2', 'phone_number2', 'address2', 'ID2', 'relationship', 'avatar']
        labels = {
            'full_name': 'Họ và tên',
            'phone_number': 'Số điện thoại',
            'nationality': 'Quốc tịch',
            'gender': 'Giới tính',
            'date_of_birth': 'Ngày sinh',
            'address': 'Địa chỉ',
            'ID1': 'Căn cước công dân/chứng minh nhân dân',
            'medical_record': 'Tiền sử bệnh lý của bệnh nhân',
            'avatar': 'Ảnh đại diện',
            'name2': 'Tên người thân',
            'phone_number2': 'Số điện thoại người thân',
            'address2': 'Địa chỉ người thân',
            'ID2': 'Căn cước công dân/chứng minh nhân dân người thân',
            'relationship': 'Mối quan hệ với người thân',
            
        }
    
class FeedbackForm (forms.ModelForm):
    class Meta:
        model = Feedback 
        fields = ['description', 'rating']
        labels = {
            'description': 'Hãy cho chúng tôi biết cảm nhận của bạn',
            'rating': 'Chấm điểm từ 1 tới 5 cho trải nghiệm của quý khách tại đây',
        }