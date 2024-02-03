from django import forms
from .models import Batch, Course_Name, Application

class Application_Form(forms.ModelForm):
    class Meta:
        model = Application
        fields = '__all__'
        
        widgets = {
            'course': forms.Select(attrs={'class': 'form-control'}),
            'batch': forms.Select(attrs={'class': 'form-control'}),
            'application_status': forms.Select(attrs={'class': 'form-control'}),
            'last_education': forms.Select(attrs={'class': 'form-control'}),
            'last_education_status': forms.Select(attrs={'class': 'form-control'}),
            
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Name'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Phone Number'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email Address'}),
            'present_address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Present Address'}),
        }


