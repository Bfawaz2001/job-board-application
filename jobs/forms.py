from django import forms
from .models import Job
from django.forms.widgets import DateInput
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'company', 'description', 'location', 'employment_type', 'application_deadline']
        widgets = {
            'application_deadline': DateInput(attrs={'type': 'date'}),
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
