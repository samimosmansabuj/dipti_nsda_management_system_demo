from django.contrib import admin
from home.models import Course, Batch

@admin.register(Course)
class Course_Name_Admin(admin.ModelAdmin):
    list_display = ['course_name', 'created_date', 'updated_date']
    list_filter = ['created_date', 'updated_date']
    search_fields = ['course_name']

@admin.register(Batch)
class Batch_Admin(admin.ModelAdmin):
    list_display = ['batch_name', 'course', 'batch_start', 'total_class', 'application_deadline']
    list_filter = ['application_deadline', 'batch_start', 'batch_end', 'updated_date']
    search_fields = ['batch_name']
