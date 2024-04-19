from django import forms 
from .models import Profile, Feedback
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from django.core.exceptions import ValidationError

        
class CustomUserCreationForm(UserCreationForm):  
    username = forms.CharField(
        label='Tên đăng nhập',
        min_length=5,
        max_length=150,
        error_messages={'required': 'Vui lòng nhập tên đăng nhập.', 'unique': 'Tên đăng nhập đã tồn tại.', 'invalid': 'Tên đăng nhập không được ít hơn 5 kí tự, không được dài quá 150 kí tự, chỉ chứa số, chữ cái và các kí tự: @, ., +, -, _'}
    )
    email = forms.EmailField(
        label='Email người dùng',
        error_messages={'required': 'Vui lòng nhập địa chỉ email.', 'unique': 'Email đã được sử dụng.', 'invalid': 'Định dạng Email không hợp lệ'}
    )
    password1 = forms.CharField(
        label='Mật khẩu',
        widget=forms.PasswordInput,
        error_messages={'required': 'Vui lòng nhập mật khẩu.'}
    )
    password2 = forms.CharField(
        label='Xác nhận mật khẩu',
        widget=forms.PasswordInput,
        error_messages={'required': 'Vui lòng nhập lại mật khẩu.', 'invalid': 'Mật khẩu không trùng khớp.'}
    )
    def clean_username(self):  
        username = self.cleaned_data['username'].lower()  
        if User.objects.filter(username=username).exists():  
            raise ValidationError("Tài khoản đã tồn tại")  
        return username  
  
    def clean_email(self):  
        email = self.cleaned_data['email'].lower()  
        if User.objects.filter(email=email).exists():  
            raise ValidationError(" Email đã được sử dụng")  
        return email  
  
    def clean_password2(self):  
        password1 = self.cleaned_data['password1']  
        password2 = self.cleaned_data['password2']  
  
        if password1 and password2 and password1 != password2:  
            raise ValidationError("Mật khẩu không trùng khớp")  
        return password2  
  
    def save(self, commit=True):  
        user = super(CustomUserCreationForm, self).save(commit=False)  
        user.email = self.cleaned_data['email']  
        if commit:  
            user.save()  
        return user          
        
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