# Generated by Django 5.2.3 on 2025-06-18 08:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('academic_app', '0010_remove_subject_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='course',
        ),
    ]
