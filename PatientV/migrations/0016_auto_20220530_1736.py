# Generated by Django 2.0 on 2022-05-30 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PatientV', '0015_auto_20220529_1251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='p_detail',
            name='Medical_History',
            field=models.CharField(default='No Medical History', max_length=250),
        ),
    ]
