# Generated by Django 5.0.1 on 2024-02-03 13:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course_Name',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=300)),
                ('image', models.ImageField(upload_to='course/image/')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batch_name', models.CharField(max_length=300)),
                ('total_class', models.PositiveIntegerField(blank=True, null=True)),
                ('total_assignment', models.PositiveIntegerField(blank=True, null=True)),
                ('application_deadline', models.DateField(blank=True, null=True)),
                ('batch_start', models.DateField(blank=True, null=True)),
                ('batch_end', models.DateField(blank=True, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='course_batch', to='home.course_name')),
            ],
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=14)),
                ('email', models.EmailField(max_length=100)),
                ('present_address', models.CharField(blank=True, max_length=600, null=True)),
                ('last_education', models.CharField(blank=True, choices=[('SSC', 'SSC'), ('HSC', 'HSC'), ('Diploma', 'Diploma'), ('Bsc', 'Bsc'), ('Honours', 'Honours'), ('Masters', 'Masters')], max_length=50, null=True)),
                ('last_education_status', models.BooleanField(default=False)),
                ('application_status', models.CharField(blank=True, choices=[('Pending', 'Pending'), ('Selected', 'Selected'), ('Cancel', 'Cancel'), ('Rejected', 'Rejected'), ('Waiting', 'Waiting')], default='Pending', max_length=50, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('batch', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='batch_applicant', to='home.batch')),
                ('course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='course_applicant', to='home.course_name')),
            ],
        ),
    ]