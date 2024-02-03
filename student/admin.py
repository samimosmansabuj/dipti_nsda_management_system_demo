from django.contrib import admin
from .models import *

@admin.register(Student_Profile)
class Student_Profile_Admin(admin.ModelAdmin):
    list_display = ['name', 'course', 'batch', 'last_education', 'phone_number', 'student_ID']
    list_filter = ['created_date', 'last_education', 'course', 'batch']
    search_fields = ['name', 'phone_number', 'email', 'present_address', 'last_education']
    
@admin.register(Student_Attendance)
class Student_Attendance_Admin(admin.ModelAdmin):
    list_display = ['date', 'status', 'student', 'batch', 'course']
    list_filter = ['date', 'status', 'student', 'batch', 'course']
    search_fields = ['date', 'status', 'student', 'batch', 'course']