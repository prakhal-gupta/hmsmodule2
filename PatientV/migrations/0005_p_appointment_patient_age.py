# Generated by Django 2.0 on 2022-05-22 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PatientV', '0004_auto_20220522_1645'),
    ]

    operations = [
        migrations.AddField(
            model_name='p_appointment',
            name='Patient_Age',
            field=models.CharField(max_length=5, null=True),
        ),
    ]