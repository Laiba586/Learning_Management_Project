# Generated by Django 5.2.3 on 2025-06-20 08:01

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academic_app', '0020_alter_studentattendance_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacherattendance',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
