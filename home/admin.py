from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Teacher)

@admin.register(Application)
class Application_Admin(admin.ModelAdmin):
    list_display = ['name', 'course', 'batch', 'last_education', 'application_status', 'created_date']
    list_filter = ['application_status', 'created_date', 'updated_date']
    search_fields = ['name', 'phone_number', 'email', 'present_address', 'last_education', 'application_status']


