from django import forms
from home.models import Teacher

class Teacher_Form(forms.ModelForm):
    username = forms.CharField(required=False, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Username'}))
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Name'}))
    phone_number = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Phone Number'}))
    email = forms.EmailField(required=False, max_length=100, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email Address'}))
    class Meta:
        model = Teacher
        fields = ['name', 'phone_number', 'last_education', 'course']
        widgets = {
            'last_education': forms.Select(attrs={
                'class': 'form-control'
            }),
            'course': forms.Select(attrs={
                'class': 'form-control'
            })
        }
