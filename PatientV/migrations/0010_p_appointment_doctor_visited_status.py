# Generated by Django 2.0 on 2022-05-25 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PatientV', '0009_p_appointment_diagnosis'),
    ]

    operations = [
        migrations.AddField(
            model_name='p_appointment',
            name='Doctor_Visited_Status',
            field=models.CharField(default='Not Visited', max_length=30),
        ),
    ]
