from django.shortcuts import render, redirect

from . forms import CreateUserForm
from django.contrib.auth.models import User
from login.models import UserData

# Create your views here.
def homepage(request):
    return render(request, 'login/index.html')

# def register(request):

    # form = CreateUserForm()

    # if request.method == "POST":

    #     form = CreateUserForm(request.POST)

        # if form.is_valid():
            
        #     form.save()

        #     return redirect("homepage")

        # if form.is_valid():
        #     form.save()
        #     username = form.cleaned_data.get('username')
        #     phone_number = form.cleaned_data.get('phone_number')
        #     gender = form.cleaned_data.get('gender')
        #     user = User.objects.get(username=username)
        #     user_data = UserData.objects.create(user=user, phone_number=phone_number, gender=gender)
        #     user_data.save()
        #     return redirect('homepage')
    
    # context = {'registerform':form}

    # return render(request, 'login/register.html', context=context)

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

def my_login(request):
    return render(request, 'login/my_login.html')

def dashboard(request):
    return render(request, 'login/dashboard.html')