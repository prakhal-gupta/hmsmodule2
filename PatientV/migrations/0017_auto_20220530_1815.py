# Generated by Django 2.0 on 2022-05-30 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PatientV', '0016_auto_20220530_1736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='p_detail',
            name='modified_at',
            field=models.DateTimeField(null=True),
        ),
    ]
