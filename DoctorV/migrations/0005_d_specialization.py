# Generated by Django 2.0 on 2022-05-25 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DoctorV', '0004_d_security'),
    ]

    operations = [
        migrations.CreateModel(
            name='D_Specialization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Specialization', models.CharField(max_length=50, null=True)),
            ],
        ),
    ]
