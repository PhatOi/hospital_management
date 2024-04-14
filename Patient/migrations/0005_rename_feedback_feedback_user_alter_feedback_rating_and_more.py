# Generated by Django 5.0.3 on 2024-04-14 14:15

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Patient', '0004_feedback'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='feedback',
            new_name='user',
        ),
        migrations.AlterField(
            model_name='feedback',
            name='rating',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]),
        ),
        migrations.CreateModel(
            name='MedicalDate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('description', models.TextField()),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TestResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('height', models.DecimalField(decimal_places=2, max_digits=6)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=6)),
                ('blood_pressure', models.DecimalField(decimal_places=2, max_digits=6)),
                ('heart_rate', models.DecimalField(decimal_places=2, max_digits=6)),
                ('blood_test', models.CharField(max_length=100)),
                ('urinalysis', models.CharField(max_length=100)),
                ('conclusion', models.TextField()),
                ('patient', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
