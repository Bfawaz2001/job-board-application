from django import forms
from .models import Job
from django.forms.widgets import DateInput

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'company', 'description', 'location', 'employment_type', 'application_deadline']
        widgets = {
            'application_deadline': DateInput(attrs={'type': 'date'}),
        }
