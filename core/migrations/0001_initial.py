# Generated by Django 3.0.8 on 2020-07-01 20:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=50)),
                ('first_name', models.CharField(max_length=50)),
                ('sex', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('U', 'Unknown')], default='U', max_length=1)),
                ('age', models.IntegerField()),
                ('phone', models.CharField(default='1', max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('heard_of_stand', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default='N', max_length=1)),
                ('heard_of_stand_how', models.CharField(blank=True, max_length=200)),
                ('refugee_ever', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default='N', max_length=1)),
                ('refugee_reason', models.CharField(blank=True, max_length=500)),
                ('recent_earthquake', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default='N', max_length=1)),
                ('previous_patient', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default='N', max_length=1)),
                ('pregnant', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default='N', max_length=1)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('chief_complaint', models.TextField(max_length=500)),
                ('my_order', models.PositiveIntegerField(default=0)),
                ('status', models.CharField(choices=[('W', 'Waiting'), ('B', 'Being Seen'), ('D', 'Discharged'), ('NS', 'No Show'), ('R', 'Returning later')], default='W', max_length=2)),
                ('department', models.CharField(choices=[('PT', 'Physical Therapy'), ('GM', 'Gen Med'), ('W', 'Wound'), ('P1', 'Prosthetics'), ('P2', 'Peds'), ('P3', 'Pelvic')], default='PT', max_length=2)),
                ('photo_permission', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default='N', max_length=1)),
                ('card_ID', models.IntegerField()),
                ('order_ID', models.IntegerField(default=0)),
                ('provider_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('my_order', '-order_ID', 'card_ID', 'id'),
            },
        ),
        migrations.CreateModel(
            name='pain_catastrophizing_scale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('q1_pcs', models.IntegerField(choices=[(-5, '-5'), (-4, '-4'), (-3, '-3'), (-2, '-2'), (-1, -1), (0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('q2_pcs', models.IntegerField(choices=[(-5, '-5'), (-4, '-4'), (-3, '-3'), (-2, '-2'), (-1, -1), (0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('q3_pcs', models.IntegerField(choices=[(-5, '-5'), (-4, '-4'), (-3, '-3'), (-2, '-2'), (-1, -1), (0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('q4_pcs', models.IntegerField(choices=[(-5, '-5'), (-4, '-4'), (-3, '-3'), (-2, '-2'), (-1, -1), (0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('q5_pcs', models.IntegerField(choices=[(-5, '-5'), (-4, '-4'), (-3, '-3'), (-2, '-2'), (-1, -1), (0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('q6_pcs', models.IntegerField(choices=[(-5, '-5'), (-4, '-4'), (-3, '-3'), (-2, '-2'), (-1, -1), (0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('q7_pcs', models.IntegerField(choices=[(-5, '-5'), (-4, '-4'), (-3, '-3'), (-2, '-2'), (-1, -1), (0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('q8_pcs', models.IntegerField(choices=[(-5, '-5'), (-4, '-4'), (-3, '-3'), (-2, '-2'), (-1, -1), (0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('q9_pcs', models.IntegerField(choices=[(-5, '-5'), (-4, '-4'), (-3, '-3'), (-2, '-2'), (-1, -1), (0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('q10_pcs', models.IntegerField(choices=[(-5, '-5'), (-4, '-4'), (-3, '-3'), (-2, '-2'), (-1, -1), (0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('q11_pcs', models.IntegerField(choices=[(-5, '-5'), (-4, '-4'), (-3, '-3'), (-2, '-2'), (-1, -1), (0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('q12_pcs', models.IntegerField(choices=[(-5, '-5'), (-4, '-4'), (-3, '-3'), (-2, '-2'), (-1, -1), (0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('q13_pcs', models.IntegerField(choices=[(-5, '-5'), (-4, '-4'), (-3, '-3'), (-2, '-2'), (-1, -1), (0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('my_order', models.PositiveIntegerField(default=0)),
                ('patient_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.patient')),
                ('provider_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['my_order', '-patient_id'],
            },
        ),
        migrations.CreateModel(
            name='encounter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Back_Pain', models.BooleanField(default=False)),
                ('general_pain', models.BooleanField(default=False)),
                ('medication_list', models.TextField(default='none', max_length=500)),
                ('Cane', models.BooleanField(default=False)),
                ('Crutches', models.BooleanField(default=False)),
                ('Walker', models.BooleanField(default=False)),
                ('Wheel_Chair', models.BooleanField(default=False)),
                ('Manual_Therapy', models.BooleanField(default=False)),
                ('Education', models.BooleanField(default=False)),
                ('Exercise', models.BooleanField(default=False)),
                ('Improvement', models.IntegerField(choices=[(-5, '-5'), (-4, '-4'), (-3, '-3'), (-2, '-2'), (-1, -1), (0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('Systolic', models.CharField(blank=True, default='0', max_length=4)),
                ('Diastolic', models.CharField(blank=True, default='0', max_length=4)),
                ('Infection_UTI', models.BooleanField(default=False)),
                ('Infection_Vaginal', models.BooleanField(default=False)),
                ('Infection_Other', models.BooleanField(default=False)),
                ('Gen_Med', models.BooleanField(default=False)),
                ('Orthotics', models.BooleanField(default=False)),
                ('Prosthetics', models.BooleanField(default=False)),
                ('Refer_Out_Of_Stand', models.BooleanField(default=False)),
                ('Neuro', models.BooleanField(default=False)),
                ('Peds', models.BooleanField(default=False)),
                ('Wound', models.BooleanField(default=False)),
                ('Gen_PT', models.BooleanField(default=False)),
                ('Pelvic_Health', models.BooleanField(default=False)),
                ('Provider_Notes', models.TextField(max_length=2000)),
                ('Supplies_Used', models.TextField(default='none', max_length=500)),
                ('Shoulder', models.BooleanField(default=False)),
                ('Wrist', models.BooleanField(default=False)),
                ('Knee', models.BooleanField(default=False)),
                ('Elbow', models.BooleanField(default=False)),
                ('Back', models.BooleanField(default=False)),
                ('Ankle', models.BooleanField(default=False)),
                ('AFO', models.BooleanField(default=False)),
                ('Shoes', models.BooleanField(default=False)),
                ('Return', models.BooleanField(default=False)),
                ('Discharged', models.BooleanField(default=False)),
                ('Refer_Out', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('my_order', models.PositiveIntegerField(default=0)),
                ('patient_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.patient')),
                ('provider_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('my_order',),
            },
        ),
        migrations.CreateModel(
            name='DischargedPatient',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('core.patient',),
        ),
        migrations.CreateModel(
            name='GMPatient',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('core.patient',),
        ),
        migrations.CreateModel(
            name='PedsPatient',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('core.patient',),
        ),
        migrations.CreateModel(
            name='PelvicPatient',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('core.patient',),
        ),
        migrations.CreateModel(
            name='ProsthPatient',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('core.patient',),
        ),
        migrations.CreateModel(
            name='PTPatient',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('core.patient',),
        ),
        migrations.CreateModel(
            name='TodayPatient',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('core.patient',),
        ),
        migrations.CreateModel(
            name='WaitingPatient',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('core.patient',),
        ),
        migrations.CreateModel(
            name='WoundPatient',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('core.patient',),
        ),
    ]
