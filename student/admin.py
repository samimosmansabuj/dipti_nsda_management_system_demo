from django.contrib import admin
from .models import *

@admin.register(Student_Profile)
class Student_Profile_Admin(admin.ModelAdmin):
    list_display = ['name', 'course', 'batch', 'last_education', 'phone_number', 'student_user']
    list_filter = ['created_date', 'last_education', 'course', 'batch']
    search_fields = ['name', 'phone_number', 'email', 'present_address', 'last_education']
    
@admin.register(Student_Attendance)
class Student_Attendance_Admin(admin.ModelAdmin):
    list_display = ['date', 'status', 'student']
    list_filter = ['date', 'status', 'student']
    search_fields = ['date', 'status', 'student']

@admin.register(Teacher_Attendance)
class Teacher_Attendance_Admin(admin.ModelAdmin):
    list_display = ['date', 'status', 'teacher']
    list_filter = ['date', 'status', 'teacher']
    search_fields = ['date', 'status', 'teacher']

