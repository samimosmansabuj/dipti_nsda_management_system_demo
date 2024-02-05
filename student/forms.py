from django import forms
from .models import Student_Profile
from home.models import *

class Student_Filter_Form(forms.Form):
    batch = forms.ModelChoiceField(queryset=Batch.objects.all(), required=False, widget=forms.Select(attrs={
        'class': 'form-control'
    }))
    course = forms.ModelChoiceField(queryset=Course_Name.objects.all(), required=False, widget=forms.Select(attrs={
        'class': 'form-control'
    }))
    search = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Search'
    }))
    
    

class Student_Form(forms.ModelForm):
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Enter Username'
    }))
    profile_picture = forms.ImageField(required=False, widget=forms.FileInput(attrs={
        'class': 'form-control'
    }))
    email = forms.EmailField(max_length=150, widget=forms.EmailInput(attrs={
        'class': 'form-control', 'placeholder': 'Enter Email Address'
    }))
    
    class Meta:
        model = Student_Profile
        fields = ['course', 'batch', 'name', 'phone_number', 'profile_picture', 'present_address', 'last_education', 'last_education_status']
        
        widgets = {
            'course': forms.Select(attrs={'class': 'form-control'}),
            'batch': forms.Select(attrs={'class': 'form-control'}),
            'last_education': forms.Select(attrs={'class': 'form-control'}),
            'last_education_status': forms.Select(attrs={'class': 'form-control'}),
            
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Name'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Phone Number'}),
            'present_address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Present Address'}),
        }