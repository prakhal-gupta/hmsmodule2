# Generated by Django 2.0 on 2022-05-22 12:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='P_Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Medical_History', models.CharField(max_length=50, null=True)),
                ('Payment_History', models.CharField(max_length=50, null=True)),
                ('Patient_Disease', models.CharField(max_length=120, null=True)),
                ('Appointment_Status', models.CharField(max_length=50, null=True)),
                ('Appointment_date', models.CharField(max_length=50, null=True)),
                ('Appointment_time', models.CharField(max_length=50, null=True)),
                ('Appointed_Doctor', models.CharField(max_length=50, null=True)),
                ('Prescription', models.CharField(max_length=50, null=True)),
                ('Registered_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='P_Detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=50, null=True)),
                ('Last_Name', models.CharField(max_length=50, null=True)),
                ('Username', models.CharField(max_length=50, null=True)),
                ('DOB', models.CharField(max_length=50, null=True)),
                ('Email', models.EmailField(max_length=254, null=True)),
                ('Password', models.CharField(max_length=120, null=True)),
                ('Mobile_Number', models.CharField(max_length=10, null=True)),
                ('Gender', models.CharField(max_length=20, null=True)),
                ('Government_ID', models.CharField(max_length=50, null=True)),
                ('Gov_ID_Number', models.CharField(max_length=50, null=True)),
                ('Height', models.CharField(max_length=20, null=True)),
                ('Weight', models.CharField(max_length=20, null=True)),
                ('Disease', models.CharField(max_length=120, null=True)),
                ('Blood_Group', models.CharField(max_length=10, null=True)),
                ('Address', models.CharField(max_length=50, null=True)),
                ('City', models.CharField(max_length=50, null=True)),
                ('State', models.CharField(max_length=50, null=True)),
                ('Country', models.CharField(max_length=50, null=True)),
                ('Pincode', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='P_Security',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=50, null=True)),
                ('Token', models.CharField(max_length=30, null=True)),
                ('Generated_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('Patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PatientV.P_Detail')),
            ],
        ),
        migrations.AddField(
            model_name='p_appointment',
            name='Patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PatientV.P_Detail'),
        ),
    ]