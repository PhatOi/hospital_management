from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from django.forms.widgets import DateInput, TextInput, CheckboxInput
from phonenumber_field.formfields import PhoneNumberField
from .models import *


class FormSettings(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FormSettings, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'

class CustomUserForm(FormSettings):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True, label='Tên')
    last_name = forms.CharField(required=True, label='Họ')
    password = forms.CharField(widget=forms.PasswordInput(), label='Mật khẩu')

    def __init__(self, *args, **kwargs):
        super(CustomUserForm, self).__init__(*args, **kwargs)

        if kwargs.get('instance'):
            instance = kwargs.get('instance').admin.__dict__
            self.fields['password'].required = False
            for field in CustomUserForm.Meta.fields:
                self.fields[field].initial = instance.get(field)
            if self.instance.pk is not None:
                self.fields['password'].widget.attrs['placeholder'] = "Chỉ điền khi bạn muốn thay đổi mật khẩu"


    class Meta:
        model = CustomUser
        fields = ['last_name', 'first_name',  'email', 'password']


class AdminForm(CustomUserForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta(CustomUserForm.Meta):
        fields = CustomUserForm.Meta.fields

class StaffForm(CustomUserForm):
    certificate = forms.CharField(max_length=255, label='Bằng cấp')
    # certificate = forms.MultipleChoiceField(choices=[], widget=TextInput)
    specialize = forms.MultipleChoiceField(choices=TreatmentFacility.facility_choices, label='Khoa chuyên môn (giữ phím ctrl để chọn nhiều hơn một)')
    available = forms.BooleanField(widget=CheckboxInput, label='Sẵn có')
    phone = PhoneNumberField()
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        instance = kwargs.get('instance')
        # Set the initial value of A to the selected choices of the instance
        if instance:
            self.fields['certificate'].initial = [c.name for c in instance.certificates.all()]
            self.fields['specialize'].initial = [s.name for s in instance.specialize.all()]
        

    class Meta(CustomUserForm.Meta):
        model = Staff
        fields = CustomUserForm.Meta.fields + ['birthday', 'phone', 'address', 'avatar', 'role', 'certificate', 'specialize', 'available']
        labels = {
            'birthday': 'Ngày sinh',
            'phone': 'Số điện thoại',
            'address': 'Địa chỉ',
            'avatar': 'Ảnh đại diện',
            'role': 'Vai trò',
        }
        widgets = {
            'birthday': DateInput(attrs={'type': 'date'}),
        }
    

class PatientForm(CustomUserForm):
    phone_number = PhoneNumberField()
    phone_number2 = PhoneNumberField()

    class Meta(CustomUserForm.Meta):
        model = Patient
        fields = CustomUserForm.Meta.fields + ['phone_number', 'nationality', 'gender', 'date_of_birth', 'address', 'medical_record', 'ID1', 'avatar', 'name2', 'phone_number2', 'address2', 'ID2', 'relationship', 'progress']
        labels = {
            'phone_number': 'Số điện thoại',
            'nationality': 'Quốc tịch',
            'gender': 'Giới tính',
            'date_of_birth': 'Ngày sinh',
            'address': 'Địa chỉ',
            'medical_record': 'Tiền sử bệnh lý của bệnh nhân',
            'ID1': 'Căn cước công dân/chứng minh nhân dân',
            'avatar': 'Ảnh đại diện',
            'name2': 'Tên người thân',
            'phone_number2': 'Số điện thoại người thân',
            'address2': 'Địa chỉ người thân',
            'ID2': 'Căn cước công dân/chứng minh nhân dân người thân',
            'relationship': 'Mối quan hệ với người thân',
            'progress': 'Trạng thái',
        }
        widgets = {
            'date_of_birth': DateInput(attrs={'type': 'date'}),
        }
    

class TestResultForm(FormSettings):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = TestResult
        fields = ['test_day', 'height', 'weight', 'blood_pressure', 'heart_rate', 'wbc', 'rbc', 'hb', 'hct', 'plt', 'lym', 'neut', 'leu', 'nit', 'pro', 'ery', 'glu', 'conclusion']
    
        labels = {
            'test_day': 'Ngày lấy mẫu', 
            'height': 'Chiều cao (cm)',
            'weight': 'Cân nặng (kg)',
            'blood_pressure': 'Huyết áp (mmHg)', 
            'heart_rate': 'Nhịp tim (nhịp/phút)',
            'wbc': 'Số lượng bạch cầu (G/L)',
            'rbc': 'Số lượng hồng cầu (T/L)',
            'hb': 'Lượng huyết sắc tố (g/L)',
            'hct': 'Tỷ lệ thể tích hồng cầu (%)', 
            'plt': 'Số lượng tiểu cầu (G/L)',
            'lym': 'Bạch cầu lympho (%)',
            'neut': 'Bạch cầu trung tính (%)',
            'leu': 'Nồng độ bạch cầu trong nước tiểu (Leu/UL)',
            'nit': 'Chỉ số Nitrit trong nước tiểu (mg/dL)',
            'pro': 'Chỉ số Protein trong nước tiểu (mg/dL)',
            'ery': 'Chỉ số hồng cầu trong nước tiểu (Ery/UL)',
            'glu': 'Chỉ số đường huyết (mg/dL)',
            'conclusion': 'Kết luận'         
        }
        widgets = {
            'test_day': DateInput(attrs={'type': 'date'}),
        }

class MedicalHistoryForm(FormSettings):
    class Meta:
        model = MedicalHistory
        fields = ['date', 'diagnosis', 'prescription', 'treatment_num_days', 'medical_department']
    
        labels = {
            'date': 'Ngày khám',
            'diagnosis': 'Chẩn đoán',
            'prescription': 'Toa thuốc',
            'treatment_num_days': 'Số ngày điều trị',
            'medical_department': 'Khoa điều trị'  
        }
        widgets = {
            'date': DateInput(attrs={'type': 'date'}),
        }    

class FeedbackStaffForm(FormSettings):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = FeedbackStaff
        fields = ['feedback']

        labels = {
            'feedback': 'Nội dung'
        }

class FeedbackPatientForm(FormSettings):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    class Meta:
        model = FeedbackPatient
        fields = ['feedback', 'rating']

        labels = {
            'feedback': 'Nội dung',
            'rating': 'Đánh giá của bạn'
        }


class TreatmentScheduleForm(FormSettings):
    facility = forms.ChoiceField(choices=TreatmentFacility.facility_choices, label='Khoa điều trị')   

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = TreatmentSchedule
        fields = ['label', 'patient', 'facility', 'start_date', 'end_date', 'room']

        labels = {
            'label': 'Nhãn',
            'patient': 'Bệnh nhân',
            'start_date': 'Ngày bắt đầu',
            'end_date': 'Ngày kết thúc',
            'room': 'Phòng',
            'facility': 'Khoa điều trị',
        }

        widgets = {
            'start_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }