# Generated by Django 5.2.3 on 2025-06-18 13:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('academic_app', '0014_remove_classroom_subjects'),
    ]

    operations = [
        migrations.RenameField(
            model_name='classroom',
            old_name='students',
            new_name='totalstudents',
        ),
    ]
