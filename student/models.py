from django.db import models
from account.models import Custom_User
from home.models import *


class Student_Profile(models.Model):
    EDUCATION = (
        ('SSC', 'SSC'),
        ('HSC', 'HSC'),
        ('Diploma', 'Diploma'),
        ('Bsc', 'Bsc'),
        ('Honours', 'Honours'),
        ('Masters', 'Masters'),
    )
    LAST_EDUCATION_STATUS = (
        ('Complete', 'Complete'),
        ('Running', 'Running'),
        ('Stop', 'Stop'),
    )
    course = models.ForeignKey(Course, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='student_course')
    batch = models.ForeignKey(Batch, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='student_batch')
    student_user = models.OneToOneField(Custom_User, on_delete=models.CASCADE, blank=True, null=True, related_name='student_user')
    
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=14)
    profile_picture = models.ImageField(upload_to='student/image/', blank=True, null=True)
    present_address = models.CharField(max_length=600, blank=True, null=True)
    
    last_education = models.CharField(choices=EDUCATION, max_length=50, blank=True, null=True)
    last_education_status = models.CharField(max_length=20, choices=LAST_EDUCATION_STATUS, blank=True, null=True)
    
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.name


class Student_Attendance(models.Model):
    student = models.ForeignKey(Student_Profile,on_delete=models.CASCADE, blank=True, null=True, related_name='student_attendance')
    date = models.DateField()
    status = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-date']
    
    def __str__(self) -> str:
        return f'{self.student.name} - {self.date}'


class Teacher_Attendance(models.Model):
    teacher = models.ForeignKey(Student_Profile,on_delete=models.CASCADE, blank=True, null=True, related_name='Teacher_attendance')
    date = models.DateField()
    status = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-date']
    
    def __str__(self) -> str:
        return f'{self.teacher.name} - {self.date}'