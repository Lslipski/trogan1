# Generated by Django 3.0.8 on 2020-08-17 04:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20200816_1539'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gmencounter',
            old_name='Diastolic',
            new_name='GM_Diastolic',
        ),
        migrations.RenameField(
            model_name='gmencounter',
            old_name='Medicine_List',
            new_name='GM_Medicine_List',
        ),
        migrations.RenameField(
            model_name='gmencounter',
            old_name='Provider_Notes',
            new_name='GM_Provider_Notes',
        ),
        migrations.RenameField(
            model_name='gmencounter',
            old_name='Systolic',
            new_name='GM_Systolic',
        ),
        migrations.RenameField(
            model_name='gmencounter',
            old_name='patient_id',
            new_name='GM_patient_id',
        ),
    ]
