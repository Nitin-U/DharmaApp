from django.shortcuts import render, redirect

#For authentication system - register, login, logout & profile update
from . forms import CreateUserForm, UserProfileForm, UserDataForm
from django.contrib.auth.models import User
from login.models import UserData
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
#uudi generator for unique Username
import uuid
#For email verification service
from Dharma_App import settings
from django.core.mail import send_mail

# Create your views here.
########################################
# View for rendering the user dashboard
def basepage(request):
    return render(request, 'login/base.html')

#View for rendering the homepage
def homepage(request):
    return render(request, 'login/index.html')

# View for user registration
def register(request):

    if request.method == "POST":
        email = request.POST['email']
        username = request.POST['username']
        phone_number = request.POST['phone_number']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        role = request.POST['role']

        # Append a unique number to the username
        unique_number = uuid.uuid4().int % 1000  # generates a random number between 0 and 999
        username = f"{username}{unique_number}"

        # Create User instance
        myuser = User.objects.create_user(username, email, password1)
        
        # Create UserData instance and link it to the User instance
        user_data = UserData(phone_number=phone_number, role=role, user=myuser)
        user_data.save()
        # myuser.save()

        # WELCOME EMAIL
        subject = "Welcome to Dharma Saranam Gachhami " + myuser.username
        message = "Hello " + myuser.username + "! \n" + "Welcome to Dharma Saranam Gachhyyami. Your account has been created, please confirm your email now. "
        from_email = settings.EMAIL_HOST_USER
        to_list = [myuser.email]
        send_mail(subject, message, from_email, to_list, fail_silently = False)

        return redirect('homepage')


    return render(request, 'login/register.html')

# View for rendering the custom login page
def my_login(request):

    form = CreateUserForm()

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password1']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return render(request, 'login/index.html', {'username': username})

        else:
            messages.error(request, "Credential does not match")

    context = {'loginform': form}

    return render(request, 'login/my_login.html', context)

def update_user(request):

    if request.user.is_authenticated:

        current_user = User.objects.get(id = request.user.id)
        user_data = UserData.objects.get(user = current_user)

        if request.method == 'POST':
            current_user_form = UserProfileForm(request.POST or None, instance = current_user)
            user_data_form = UserDataForm(request.POST or None, instance = user_data)

            if current_user_form.is_valid() and user_data_form.is_valid():
                current_user_form.save()
                user_data_form.save()
                messages.success(request, 'Profile updated successfully')
                return redirect('dashboard')
        else:
            current_user_form = UserProfileForm(instance = current_user)
            user_data_form = UserDataForm(instance = user_data)

        return render(request, 'login/update_profile.html', {'form_user':current_user_form, 'form_userData':user_data_form})
    
    else:

        messages.success(request, ("You must be logged in to update profile"))
    

# View for rendering the user dashboard
def dashboard(request):
    return render(request, 'login/dashboard.html')

# View for Logging Out
def my_logout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully.")
    return redirect('my_login')