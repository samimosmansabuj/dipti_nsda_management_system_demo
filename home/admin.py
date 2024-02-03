from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Course_Name)
class Course_Name_Admin(admin.ModelAdmin):
    list_display = ['course_name', 'created_date', 'updated_date']
    list_filter = ['created_date', 'updated_date']
    search_fields = ['course_name']

@admin.register(Batch)
class Batch_Admin(admin.ModelAdmin):
    list_display = ['batch_name', 'course', 'batch_start', 'total_class', 'application_deadline']
    list_filter = ['application_deadline', 'batch_start', 'batch_end', 'updated_date']
    search_fields = ['batch_name']

@admin.register(Application)
class Application_Admin(admin.ModelAdmin):
    list_display = ['name', 'course', 'batch', 'last_education', 'application_status', 'created_date']
    list_filter = ['application_status', 'created_date', 'updated_date']
    search_fields = ['name', 'phone_number', 'email', 'present_address', 'last_education', 'application_status']
