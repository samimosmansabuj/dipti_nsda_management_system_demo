from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from .managers import UserManager
from django.db import models
from home.models import Course_Name

class Custom_User(AbstractBaseUser, PermissionsMixin):
    USER_TYPE = (
        ('Administration', 'Administration'),
        ('HR', 'HR'),
        ('Staff', 'Staff'),
        ('Teacher', 'Teacher'),
        ('Student', 'Student'),
    )
    name = models.CharField(max_length=100, blank=True, null=True)
    username = models.CharField(max_length=50, unique=True, validators=[UnicodeUsernameValidator])
    email = models.EmailField(max_length=50, unique=True)
    user_type = models.CharField(choices=USER_TYPE, max_length=40, blank=True, null=True)
    
    auth_token = models.CharField(max_length=200, blank=True, null=True)
    otp = models.CharField(max_length=6, blank=True, null=True)
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    objects = UserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    class Meta:
        ordering = ['-created_date']
    
    def __str__(self) -> str:
        return self.username


class Teacher(models.Model):
    EDUCATION = (
        ('SSC', 'SSC'),
        ('HSC', 'HSC'),
        ('Diploma', 'Diploma'),
        ('Bsc', 'Bsc'),
        ('Honours', 'Honours'),
        ('Masters', 'Masters'),
    )
    teacher_user = models.ForeignKey(Custom_User, related_name='teacher_user', on_delete=models.CASCADE, blank=True, null=True)
    course = models.ForeignKey(Course_Name, related_name='teacher_course', on_delete=models.CASCADE, blank=True, null=True)

    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=14, blank=True, null=True)
    last_education = models.CharField(choices=EDUCATION, max_length=50, blank=True, null=True)

    def __str__(self) -> str:
        return self.name







