# Generated by Django 3.0.8 on 2020-08-16 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20200812_1849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gmencounter',
            name='Medicine_List',
            field=models.TextField(max_length=2000),
        ),
    ]
