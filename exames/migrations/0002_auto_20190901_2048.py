# Generated by Django 2.2.4 on 2019-09-01 23:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exames', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exame',
            name='medico',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='examesFromMedico', to='roles.Medico', verbose_name='medico'),
        ),
    ]