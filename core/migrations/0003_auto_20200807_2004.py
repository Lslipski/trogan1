# Generated by Django 3.0.8 on 2020-08-07 20:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0002_userprofile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='encounter',
            old_name='Education',
            new_name='Cupping',
        ),
        migrations.RenameField(
            model_name='encounter',
            old_name='Exercise',
            new_name='Dry_Needle',
        ),
        migrations.RenameField(
            model_name='encounter',
            old_name='Manual_Therapy',
            new_name='Tape',
        ),
        migrations.CreateModel(
            name='pain_catastrophizing_scale2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('q1_pcs', models.IntegerField(choices=[(-5, '-5'), (-4, '-4'), (-3, '-3'), (-2, '-2'), (-1, -1), (0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('q2_pcs', models.IntegerField(choices=[(-5, '-5'), (-4, '-4'), (-3, '-3'), (-2, '-2'), (-1, -1), (0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('my_order', models.PositiveIntegerField(default=0)),
                ('patient_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.patient')),
                ('provider_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['my_order', '-patient_id'],
            },
        ),
    ]
