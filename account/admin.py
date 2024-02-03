from django.contrib import admin
from .models import Custom_User

@admin.register(Custom_User)
class Custom_User_Admin(admin.ModelAdmin):
    list_display = ['username', 'name', 'email', 'user_type', 'updated_date']
    list_filter = ['user_type', 'updated_date', 'created_date']
    search_fields = ['username', 'name', 'email', 'user_type']
    
