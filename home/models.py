from django.db import models

# Create your models here.
class Course_Name(models.Model):
    course_name = models.CharField(max_length=300)
    image = models.ImageField(upload_to='course/image/', blank=True, null=True)
    
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.course_name

class Batch(models.Model):
    STATUS = (
        ('Upcoming', 'Upcoming'),
        ('Running', 'Running'),
        ('Complete', 'Complete'),
        ('Cancel', 'Cancel'),
    )
    course = models.ForeignKey(Course_Name, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='course_batch')
    
    batch_name = models.CharField(max_length=300)
    total_class = models.PositiveIntegerField(blank=True, null=True)
    
    application_deadline = models.DateField(blank=True, null=True)
    batch_start = models.DateField(blank=True, null=True)
    batch_end = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=50, choices=STATUS, blank=True,null=True)
    
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.batch_name


class Application(models.Model):
    EDUCATION = (
        ('SSC', 'SSC'),
        ('HSC', 'HSC'),
        ('Diploma', 'Diploma'),
        ('Bsc', 'Bsc'),
        ('Honours', 'Honours'),
        ('Masters', 'Masters'),
    )
    APPLICATION_STATUS = (
        ('Pending', 'Pending'),
        ('Selected', 'Selected'),
        ('Cancel', 'Cancel'),
        ('Rejected', 'Rejected'),
        ('Waiting', 'Waiting'),
    )
    LAST_EDUCATION_STATUS = (
        ('Complete', 'Complete'),
        ('Running', 'Running'),
        ('Stop', 'Stop'),
    )
    course = models.ForeignKey(Course_Name, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='course_applicant')
    batch = models.ForeignKey(Batch, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='batch_applicant')
    
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=14)
    email = models.EmailField(max_length=100)
    present_address = models.CharField(max_length=600, blank=True, null=True)
    
    last_education = models.CharField(choices=EDUCATION, max_length=50, null=True, blank=True)
    last_education_status = models.CharField(max_length=20, choices=LAST_EDUCATION_STATUS, blank=True, null=True)
    
    application_status = models.CharField(choices=APPLICATION_STATUS, max_length=50, default='Pending', null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.name



