# Generated by Django 3.0.8 on 2020-08-19 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20200819_0414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gmencounter',
            name='Diastolic',
            field=models.CharField(blank=True, default='Diastolic', max_length=4),
        ),
        migrations.AlterField(
            model_name='gmencounter',
            name='Systolic',
            field=models.CharField(blank=True, default='Systolic', max_length=4),
        ),
    ]
