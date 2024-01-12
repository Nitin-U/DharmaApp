from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User

from django import forms
from .models import UserData

class CreateUserForm(UserCreationForm):
    phone_number = forms.CharField()
    role = forms.ChoiceField(choices=UserData.USER_CHOICES)
    
    class Meta:

        model = User
        fields = ['username', 'phone_number', 'role', 'email', 'password1', 'password2']