# Generated by Django 5.0.3 on 2024-04-28 16:25

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
import phonenumber_field.modelfields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='certificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='MaintenanceEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True)),
                ('date', models.DateField()),
                ('description', models.TextField()),
                ('explain', models.TextField(null=True)),
                ('maintenance_count', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('numbers', models.PositiveIntegerField()),
                ('expiry', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='MedicineHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('numbers', models.PositiveIntegerField()),
                ('changeType', models.CharField(max_length=200)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='TreatmentFacility',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Khoa khám bệnh', 'Khoa khám bệnh'), ('Khoa Hồi sức cấp cứu', 'Khoa Hồi sức cấp cứu'), ('Khoa Nội tổng hợp', 'Khoa Nội tổng hợp'), ('Khoa Nội tim mạch', 'Khoa Nội tim mạch'), ('Khoa Nội tiêu hóa', 'Khoa Nội tiêu hóa'), ('Khoa Nội cơ - xương - khớp', 'Khoa Nội cơ - xương - khớp'), ('Khoa Nội thận - tiết niệu', 'Khoa Nội thận - tiết niệu'), ('Khoa Nội tiết', 'Khoa Nội tiết'), ('Khoa Dị ứng', 'Khoa Dị ứng'), ('Khoa Truyền nhiễm', 'Khoa Truyền nhiễm'), ('Khoa Lao', 'Khoa Lao'), ('Khoa Da Liễu', 'Khoa Da Liễu'), ('Khoa Thần kinh', 'Khoa Thần kinh'), ('Khoa Tâm thần', 'Khoa Tâm thần'), ('Khoa Nhi', 'Khoa Nhi'), ('Khoa Ngoại tổng hợp', 'Khoa Ngoại tổng hợp'), ('Khoa Ngoại thần kinh', 'Khoa Ngoại thần kinh'), ('Khoa Ngoại lồng ngực', 'Khoa Ngoại lồng ngực'), ('Khoa Ngoại tiêu hóa', 'Khoa Ngoại tiêu hóa'), ('Khoa Ngoại thận - tiết niệu', 'Khoa Ngoại thận - tiết niệu'), ('Khoa Chấn thương chỉnh hình', 'Khoa Chấn thương chỉnh hình'), ('Khoa Phẩu thuật gây mê hồi sức', 'Khoa Phẩu thuật gây mê hồi sức'), ('Khoa Phụ sản', 'Khoa Phụ sản'), ('Khoa Tai - mũi - họng', 'Khoa Tai - mũi - họng'), ('Khoa Răng - hàm - mặt', 'Khoa Răng - hàm - mặt'), ('Khoa mắt', 'Khoa mắt'), ('Khoa Vật lý trị liệu - phục hồi chức năng', 'Khoa Vật lý trị liệu - phục hồi chức năng'), ('Khoa Huyến học', 'Khoa Huyến học'), ('Khoa Hóa Sinh', 'Khoa Hóa Sinh'), ('Khoa Vi sinh', 'Khoa Vi sinh'), ('Khoa Chẩn đoán hình ảnh', 'Khoa Chẩn đoán hình ảnh'), ('Khoa Thăm dò chức năng', 'Khoa Thăm dò chức năng'), ('Khoa Nội soi', 'Khoa Nội soi'), ('Khoa Chống nhiễm khuẩn', 'Khoa Chống nhiễm khuẩn'), ('Khoa Dược', 'Khoa Dược'), ('Khoa Dinh dưỡng', 'Khoa Dinh dưỡng')], max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('user_type', models.CharField(choices=[(1, 'Admin'), (2, 'Staff'), (3, 'Patient')], default=1, max_length=10)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('admin', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MedicalEquipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('numbers', models.PositiveIntegerField()),
                ('available', models.PositiveIntegerField(null=True)),
                ('maintenance_history', models.ManyToManyField(to='main_app.maintenanceevent')),
            ],
        ),
        migrations.CreateModel(
            name='Facility',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medical_equipments', models.ManyToManyField(to='main_app.medicalequipment')),
                ('medicines', models.ManyToManyField(to='main_app.medicine')),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True)),
                ('nationality', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('male', 'Nam'), ('female', 'Nữ')], max_length=10)),
                ('date_of_birth', models.DateField(null=True)),
                ('address', models.TextField()),
                ('ID1', models.CharField(max_length=30)),
                ('medical_record', models.TextField(null=True)),
                ('avatar', models.FileField(blank=True, null=True, upload_to='patient_avatar')),
                ('name2', models.CharField(max_length=100)),
                ('phone_number2', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True)),
                ('address2', models.TextField()),
                ('ID2', models.CharField(max_length=30)),
                ('relationship', models.CharField(max_length=30)),
                ('progress', models.CharField(choices=[('Đang tiếp nhận', 'Đang tiếp nhận'), ('Đang chẩn đoán', 'Đang chẩn đoán'), ('Đang điều trị', 'Đang điều trị'), ('Xuất viện', 'Xuất viện')], max_length=100, null=True)),
                ('admin', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MedicalHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('diagnosis', models.TextField()),
                ('prescription', models.TextField(null=True)),
                ('treatment_num_days', models.PositiveIntegerField(null=True)),
                ('medical_department', models.CharField(choices=[('Khoa khám bệnh', 'Khoa khám bệnh'), ('Khoa Hồi sức cấp cứu', 'Khoa Hồi sức cấp cứu'), ('Khoa Nội tổng hợp', 'Khoa Nội tổng hợp'), ('Khoa Nội tim mạch', 'Khoa Nội tim mạch'), ('Khoa Nội tiêu hóa', 'Khoa Nội tiêu hóa'), ('Khoa Nội cơ - xương - khớp', 'Khoa Nội cơ - xương - khớp'), ('Khoa Nội thận - tiết niệu', 'Khoa Nội thận - tiết niệu'), ('Khoa Nội tiết', 'Khoa Nội tiết'), ('Khoa Dị ứng', 'Khoa Dị ứng'), ('Khoa Truyền nhiễm', 'Khoa Truyền nhiễm'), ('Khoa Lao', 'Khoa Lao'), ('Khoa Da Liễu', 'Khoa Da Liễu'), ('Khoa Thần kinh', 'Khoa Thần kinh'), ('Khoa Tâm thần', 'Khoa Tâm thần'), ('Khoa Nhi', 'Khoa Nhi'), ('Khoa Ngoại tổng hợp', 'Khoa Ngoại tổng hợp'), ('Khoa Ngoại thần kinh', 'Khoa Ngoại thần kinh'), ('Khoa Ngoại lồng ngực', 'Khoa Ngoại lồng ngực'), ('Khoa Ngoại tiêu hóa', 'Khoa Ngoại tiêu hóa'), ('Khoa Ngoại thận - tiết niệu', 'Khoa Ngoại thận - tiết niệu'), ('Khoa Chấn thương chỉnh hình', 'Khoa Chấn thương chỉnh hình'), ('Khoa Phẩu thuật gây mê hồi sức', 'Khoa Phẩu thuật gây mê hồi sức'), ('Khoa Phụ sản', 'Khoa Phụ sản'), ('Khoa Tai - mũi - họng', 'Khoa Tai - mũi - họng'), ('Khoa Răng - hàm - mặt', 'Khoa Răng - hàm - mặt'), ('Khoa mắt', 'Khoa mắt'), ('Khoa Vật lý trị liệu - phục hồi chức năng', 'Khoa Vật lý trị liệu - phục hồi chức năng'), ('Khoa Huyến học', 'Khoa Huyến học'), ('Khoa Hóa Sinh', 'Khoa Hóa Sinh'), ('Khoa Vi sinh', 'Khoa Vi sinh'), ('Khoa Chẩn đoán hình ảnh', 'Khoa Chẩn đoán hình ảnh'), ('Khoa Thăm dò chức năng', 'Khoa Thăm dò chức năng'), ('Khoa Nội soi', 'Khoa Nội soi'), ('Khoa Chống nhiễm khuẩn', 'Khoa Chống nhiễm khuẩn'), ('Khoa Dược', 'Khoa Dược'), ('Khoa Dinh dưỡng', 'Khoa Dinh dưỡng')], max_length=255, null=True)),
                ('patient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.patient')),
            ],
        ),
        migrations.CreateModel(
            name='FeedbackPatient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback', models.TextField()),
                ('reply', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('rating', models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=0)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('birthday', models.DateField(null=True)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True)),
                ('address', models.TextField()),
                ('avatar', models.FileField(blank=True, null=True, upload_to='staff_avatar')),
                ('role', models.CharField(choices=[('Bác sĩ', 'Bác sĩ'), ('Y tá', 'Y tá'), ('Khác', 'Khác')], max_length=15)),
                ('available', models.BooleanField(null=True)),
                ('admin', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('certificates', models.ManyToManyField(to='main_app.certificate')),
                ('specialize', models.ManyToManyField(to='main_app.treatmentfacility')),
            ],
        ),
        migrations.CreateModel(
            name='NotificationStaff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.staff')),
            ],
        ),
        migrations.CreateModel(
            name='FeedbackStaff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback', models.TextField()),
                ('reply', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.staff')),
            ],
        ),
        migrations.CreateModel(
            name='TestResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_day', models.DateField(null=True)),
                ('height', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('blood_pressure', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('heart_rate', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('wbc', models.PositiveIntegerField(null=True)),
                ('rbc', models.PositiveIntegerField(null=True)),
                ('hb', models.PositiveIntegerField(null=True)),
                ('hct', models.PositiveIntegerField(null=True)),
                ('plt', models.PositiveIntegerField(null=True)),
                ('lym', models.PositiveIntegerField(null=True)),
                ('neut', models.PositiveIntegerField(null=True)),
                ('leu', models.PositiveIntegerField(null=True)),
                ('nit', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('pro', models.DecimalField(decimal_places=3, max_digits=6, null=True)),
                ('ery', models.PositiveIntegerField(null=True)),
                ('glu', models.PositiveIntegerField(null=True)),
                ('conclusion', models.TextField()),
                ('patient', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.patient')),
            ],
        ),
        migrations.CreateModel(
            name='TreatmentSchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(choices=[('Cuộc hẹn', 'Cuộc hẹn'), ('Điều trị', 'Điều trị')], max_length=30, null=True)),
                ('start_date', models.DateTimeField(null=True)),
                ('duration', models.PositiveIntegerField(null=True)),
                ('end_date', models.DateTimeField(null=True)),
                ('room', models.CharField(max_length=10)),
                ('facility', models.CharField(choices=[('Khoa khám bệnh', 'Khoa khám bệnh'), ('Khoa Hồi sức cấp cứu', 'Khoa Hồi sức cấp cứu'), ('Khoa Nội tổng hợp', 'Khoa Nội tổng hợp'), ('Khoa Nội tim mạch', 'Khoa Nội tim mạch'), ('Khoa Nội tiêu hóa', 'Khoa Nội tiêu hóa'), ('Khoa Nội cơ - xương - khớp', 'Khoa Nội cơ - xương - khớp'), ('Khoa Nội thận - tiết niệu', 'Khoa Nội thận - tiết niệu'), ('Khoa Nội tiết', 'Khoa Nội tiết'), ('Khoa Dị ứng', 'Khoa Dị ứng'), ('Khoa Truyền nhiễm', 'Khoa Truyền nhiễm'), ('Khoa Lao', 'Khoa Lao'), ('Khoa Da Liễu', 'Khoa Da Liễu'), ('Khoa Thần kinh', 'Khoa Thần kinh'), ('Khoa Tâm thần', 'Khoa Tâm thần'), ('Khoa Nhi', 'Khoa Nhi'), ('Khoa Ngoại tổng hợp', 'Khoa Ngoại tổng hợp'), ('Khoa Ngoại thần kinh', 'Khoa Ngoại thần kinh'), ('Khoa Ngoại lồng ngực', 'Khoa Ngoại lồng ngực'), ('Khoa Ngoại tiêu hóa', 'Khoa Ngoại tiêu hóa'), ('Khoa Ngoại thận - tiết niệu', 'Khoa Ngoại thận - tiết niệu'), ('Khoa Chấn thương chỉnh hình', 'Khoa Chấn thương chỉnh hình'), ('Khoa Phẩu thuật gây mê hồi sức', 'Khoa Phẩu thuật gây mê hồi sức'), ('Khoa Phụ sản', 'Khoa Phụ sản'), ('Khoa Tai - mũi - họng', 'Khoa Tai - mũi - họng'), ('Khoa Răng - hàm - mặt', 'Khoa Răng - hàm - mặt'), ('Khoa mắt', 'Khoa mắt'), ('Khoa Vật lý trị liệu - phục hồi chức năng', 'Khoa Vật lý trị liệu - phục hồi chức năng'), ('Khoa Huyến học', 'Khoa Huyến học'), ('Khoa Hóa Sinh', 'Khoa Hóa Sinh'), ('Khoa Vi sinh', 'Khoa Vi sinh'), ('Khoa Chẩn đoán hình ảnh', 'Khoa Chẩn đoán hình ảnh'), ('Khoa Thăm dò chức năng', 'Khoa Thăm dò chức năng'), ('Khoa Nội soi', 'Khoa Nội soi'), ('Khoa Chống nhiễm khuẩn', 'Khoa Chống nhiễm khuẩn'), ('Khoa Dược', 'Khoa Dược'), ('Khoa Dinh dưỡng', 'Khoa Dinh dưỡng')], max_length=255, null=True)),
                ('patient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.patient')),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.staff')),
            ],
        ),
    ]
