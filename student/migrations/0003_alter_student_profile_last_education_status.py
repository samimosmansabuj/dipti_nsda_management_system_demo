# Generated by Django 5.0.1 on 2024-02-03 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_alter_student_profile_student_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_profile',
            name='last_education_status',
            field=models.CharField(blank=True, choices=[('Complete', 'Complete'), ('Running', 'Running'), ('Stop', 'Stop')], max_length=20, null=True),
        ),
    ]