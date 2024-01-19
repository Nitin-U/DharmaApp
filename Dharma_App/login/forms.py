from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User
from django import forms
from .models import UserData

# Built-in function User Creation Form for authentication
class CreateUserForm(UserCreationForm):
    """
    Custom user creation form extending the built-in UserCreationForm.

    Additional fields:
    - phone_number: User's phone number.
    - role: User's role, selected from predefined choices in UserData.USER_CHOICES.

    Meta:
    - model: User model for data storage.
    - fields: List of fields to be included in the form.

    Attributes:
    - phone_number (CharField): Field for capturing the user's phone number.
    - role (ChoiceField): Field for selecting the user's role from predefined choices.
    """

    phone_number = forms.CharField()
    role = forms.ChoiceField(choices=UserData.USER_CHOICES)

    class Meta:

        model = User
        fields = ['username', 'phone_number', 'role', 'email', 'password1', 'password2']

# UserProfileForm function to render fields from User Model during User Update on user profile form
class UserProfileForm(forms.ModelForm):
    # username = forms.CharField(max_length=20, required=True)
    # email = forms.EmailField(required=True)

    username = forms.CharField(max_length=20, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email']

# UserDataForm function to render fields from UserData Model during User Update on user profile form
class UserDataForm(forms.ModelForm):
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    role = forms.ChoiceField(choices=UserData.USER_CHOICES, widget=forms.Select(attrs={'class': 'form-select'}))

    class Meta:
        model = UserData
        fields = ['phone_number', 'role']
        