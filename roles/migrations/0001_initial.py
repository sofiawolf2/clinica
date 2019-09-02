# Generated by Django 2.2.4 on 2019-09-01 14:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClinicUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('nome', models.CharField(max_length=30, unique=True, verbose_name='nome')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_patient', models.BooleanField(default=False)),
                ('is_doctor', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('clinicuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('crm', models.CharField(max_length=4, unique=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('roles.clinicuser',),
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('clinicuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('rg', models.CharField(max_length=7, unique=True)),
                ('cpf', models.CharField(max_length=11, unique=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('roles.clinicuser',),
        ),
    ]