# Generated by Django 5.2.3 on 2025-06-17 11:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academic_app', '0007_remove_course_teacher_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', to='academic_app.course'),
        ),
    ]
