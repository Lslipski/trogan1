# Generated by Django 3.0.8 on 2020-08-17 04:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20200817_0432'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gmencounter',
            old_name='GM_patient_id',
            new_name='patient_id',
        ),
    ]