from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Company, JobSeeker, Job, Application

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class CompanyRegisterForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'description', 'website', 'logo']

class JobSeekerRegisterForm(forms.ModelForm):
    class Meta:
        model = JobSeeker
        fields = ['resume', 'skills', 'experience']

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'description', 'location', 'job_type', 'closing_date']
        widgets = {
            'closing_date': forms.DateInput(attrs={'type': 'date'}),
        }

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['cover_letter']