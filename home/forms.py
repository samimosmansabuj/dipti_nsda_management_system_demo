from collections.abc import Mapping
from typing import Any
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from .models import Batch, Course_Name, Application
from .models import Course_Name

class Application_Form(forms.ModelForm):
    course = forms.ModelChoiceField(queryset=Course_Name.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email Address'}), required=False)
    class Meta:
        model = Application
        fields = ['course', 'batch', 'name', 'phone_number', 'email', 'present_address', 'last_education', 'last_education_status', 'application_status']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Name'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Phone Number'}),
            'present_address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Present Address'}),
            
            'batch': forms.Select(attrs={'class': 'form-control'}),
            'last_education': forms.Select(attrs={'class': 'form-control'}),
            'last_education_status': forms.Select(attrs={'class': 'form-control'}),
            'application_status': forms.Select(attrs={'class': 'form-control'}),
        }
    
    
    def __init__(self, *args, **kwargs):
        super(Application_Form, self).__init__(*args, **kwargs)
        if 'initial' in kwargs and 'course' in kwargs['initial']:
            self.fields['batch'].queryset = kwargs['initial']['course'].course_batch.all()


