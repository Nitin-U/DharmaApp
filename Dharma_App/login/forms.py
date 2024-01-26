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

    # Custom validations for username that checks for digits only value
    def check_digits_only(value):
        if value.isdigit():
            raise forms.ValidationError("Username cannot contain only digits")
        
    # Custom validations for email that checks if email matches the database value
    def check_email_exists(value):
        if User.objects.filter(email__iexact=value).exists():
            raise forms.ValidationError("Email already exists, Please choose a different one")
        
    # Custom validations for phone number that checks the digit length
    def validate_phone_number_length(value):
        if len(value) > 10:
            raise forms.ValidationError(('Phone number must not exceed 10 digits'),
                code='invalid_phone_number_length'
            )
        
    # Custom validations for phone number that checks for non-numeric values
    def validate_phone_number_numeric(value):
        if not value.isdigit():
            raise forms.ValidationError(('Phone number must contain only numeric digits'),
                code='invalid_phone_number_format'
            )
        
    # Custom validations for phone number that checks what digits the phone number starts with
    def validate_phone_number_start(value):
        if not value.startswith('98'):
            raise forms.ValidationError(('Phone number must start with "98"'),
                code='invalid_phone_number_start'
            )


    username = forms.CharField(max_length=124, validators=[check_digits_only], widget=forms.TextInput(attrs={'class': 'p-2 form-control rounded-pill shadow-sm px-4 text-dark', 'placeholder': 'Enter Your Username' }))

    email = forms.EmailField(validators=[check_email_exists], widget=forms.EmailInput(attrs={'class': 'p-2 form-control rounded-pill shadow-sm px-4 text-dark', 'placeholder': 'Enter Your Email' }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'p-2 form-control rounded-pill shadow-sm px-4 text-dark', 'placeholder': 'Enter Your Password' }))
    
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'p-2 form-control rounded-pill shadow-sm px-4 text-dark', 'placeholder': 'Confirm Your Password' }))
    
    phone_number = forms.CharField(validators=[validate_phone_number_length, validate_phone_number_numeric, validate_phone_number_start], widget=forms.TextInput(attrs={'class': 'p-2 form-control rounded-pill shadow-sm px-4 text-dark', 'placeholder': 'Enter Your Phone Number' }))
    
    role = forms.ChoiceField(choices=UserData.USER_CHOICES, widget=forms.Select(attrs={'class': 'p-2 form-select rounded-pill shadow-sm px-4 text-muted', 'placeholder': 'Confirm Your Password' }))

    
    class Meta:

        model = User
        fields = ['username', 'phone_number', 'role', 'email', 'password1', 'password2']

#
class LoginForm(forms.Form):
    username = forms.CharField(max_length=124, validators=[], widget=forms.TextInput(attrs={'class': 'p-2 form-control rounded-pill shadow-sm px-4 text-dark', 'placeholder': 'Enter Your Username' }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'p-2 form-control rounded-pill shadow-sm px-4 text-dark', 'placeholder': 'Enter Your Password' }))

# UserProfileForm class to render fields from User Model during User Update on user profile form
class UserProfileForm(forms.ModelForm):
    # username = forms.CharField(max_length=20, required=True)
    # email = forms.EmailField(required=True)

    username = forms.CharField(max_length=20, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email']

# UserDataForm class to render fields from UserData Model during User Update on user profile form
class UserDataForm(forms.ModelForm):
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    role = forms.ChoiceField(choices=UserData.USER_CHOICES, widget=forms.Select(attrs={'class': 'form-select'}))

    class Meta:
        model = UserData
        fields = ['phone_number', 'role']
        