# Generated by Django 2.0 on 2022-05-27 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PatientV', '0012_remove_p_detail_disease'),
    ]

    operations = [
        migrations.AddField(
            model_name='p_appointment',
            name='Appointment_mod_at',
            field=models.DateTimeField(null=True),
        ),
    ]
