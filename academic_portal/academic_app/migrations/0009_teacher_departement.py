# Generated by Django 5.2.3 on 2025-06-18 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academic_app', '0008_alter_student_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='departement',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
