from .models import Job
from django.forms.widgets import DateInput
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from .models import Application


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'company', 'location', 'employment_type', 'working_condition', 'description', 'application_deadline']
        widgets = {
            'employment_type': forms.Select(choices=Job.EMPLOYMENT_TYPE_CHOICES),
            'working_condition': forms.Select(choices=Job.WORKING_CONDITION_CHOICES),
            'description': forms.Textarea(attrs={'rows': 4}),
            'application_deadline': forms.DateInput(attrs={'type': 'date'}),
            'location': forms.TextInput()  # Changed to TextInput
        }


class SignUpForm(UserCreationForm):
    user_type = forms.ChoiceField(choices=Profile.USER_TYPE_CHOICES, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'user_type']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio']


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['resume', 'cover_letter']


class ApplicantProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']  # Add any other fields you want to include


class ApplicationStatusForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['status']