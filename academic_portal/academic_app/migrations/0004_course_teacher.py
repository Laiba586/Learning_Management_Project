# Generated by Django 5.2.3 on 2025-06-15 06:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academic_app', '0003_course_image_subject_image_teacher_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='academic_app.teacher'),
        ),
    ]
