from django.shortcuts import render, redirect

from . forms import CreateUserForm
from django.contrib.auth.models import User
from login.models import UserData

# Create your views here.
#
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

        # Create User instance
        myuser = User.objects.create_user(username, email, password1)
        
        # Create UserData instance and link it to the User instance
        user_data = UserData(phone_number=phone_number, role=role, user=myuser)
        user_data.save()
        # myuser.save()

        return redirect('homepage')


    return render(request, 'login/register.html')

# View for rendering the custom login page
def my_login(request):
    return render(request, 'login/my_login.html')

# View for rendering the user dashboard
def dashboard(request):
    return render(request, 'login/dashboard.html')