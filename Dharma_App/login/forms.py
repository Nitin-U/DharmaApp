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
        

    firstname = forms.CharField(max_length=124, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your First Name Here . . .' }))

    middlename = forms.CharField(max_length=124, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Middle Name Here . . .' }), required=False)

    lastname = forms.CharField(max_length=124, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Last Name Here . . .' }))

    username = forms.CharField(max_length=124, validators=[check_digits_only], widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your User Name Here . . .' }))

    email = forms.EmailField(validators=[check_email_exists], widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Email Here . . .' }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Password Here . . .' }))
    
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Your Password . . .' }))
    
    phone_number = forms.CharField(validators=[validate_phone_number_length, validate_phone_number_numeric], widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Phone Number . . .' }))

    role = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-check-input' }), required=False)

    # user_image = forms.ImageField(required=False, widget=forms.FileInput(attrs={'class':'form-control', 'type':'file'}))
    user_image = forms.ImageField(required=False)
    
    class Meta:

        model = User
        fields = ['firstname', 'lastname', 'username', 'phone_number', 'role', 'email', 'password1', 'password2', 'user_image']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'autofocus': False})
        self.fields['firstname'].widget.attrs.update({'autofocus': True})

#Class to render login form
class LoginForm(forms.Form):
    username = forms.CharField(max_length=124, validators=[], widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Username' }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Password' }))

#Class to render User Model default fields onto profile page
class ProfileForm(forms.ModelForm):
    username = forms.CharField(max_length=20, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=20, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=20, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=False, widget=forms.EmailInput(attrs={'class': 'form-control-plaintext', 'type': 'text', 'readonly': 'readonly'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

#Class to render User Model's extra fields onto profile page
class ProfileExtraFieldsForm(forms.ModelForm):
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    role = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly' }), required=False)
    middlename = forms.CharField(max_length=124, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Middlename' }), required=False)
    contact_address = forms.CharField(max_length=124, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Contact Address . . .' }), required=False)
    mailing_address = forms.CharField(max_length=124, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Mailing Address . . .' }), required=False)
    user_image = forms.ImageField(required=False, widget=forms.FileInput(attrs={'class':'form-control'}))
    
    class Meta:
        model = UserData
        fields = ['phone_number', 'role', 'middlename', 'contact_address', 'mailing_address', 'user_image']

        