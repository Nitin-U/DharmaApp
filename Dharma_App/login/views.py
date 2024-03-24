from django.shortcuts import render, redirect
from django.urls import reverse

#For authentication system - register, login, logout & profile update
from . forms import CreateUserForm, LoginForm, ProfileForm, ProfileExtraFieldsForm
from django.contrib.auth.models import User
from login.models import UserData
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
#uudi generator for unique Username
import uuid
#For email verification service
from Dharma_App import settings
from django.core.mail import send_mail, EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from . tokens import generate_token

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
    if request.user.is_authenticated:
        return render (request, 'login/index.html')

    if request.method == "POST":
        print(request.POST)
        form = CreateUserForm(request.POST, request.FILES)
        if form.is_valid():

            # Create User instance
            myuser = User.objects.create_user(username=form.cleaned_data['username'], first_name=form.cleaned_data['firstname'], last_name=form.cleaned_data['lastname'], password=form.cleaned_data['password1'], email=form.cleaned_data['email'])
            myuser.is_active = False
            myuser.save()

            # Create UserData instance and link it to the User instance
            if form.cleaned_data['role']:
                role = 'seller'
            else:
                role = 'customer'
            user_data = UserData(phone_number=form.cleaned_data['phone_number'], role=role, middlename=form.cleaned_data['middlename'], user=myuser)
            user_data.save()

            # WELCOME EMAIL
            subject = "Welcome to Dharma Saranam Gachhami " + myuser.username
            message = "Hello " + myuser.username + "! \n" + "Welcome to Dharma Saranam Gachhyyami. Your account has been created, please confirm your email now. "
            from_email = settings.EMAIL_HOST_USER
            to_list = [myuser.email]
            send_mail(subject, message, from_email, to_list, fail_silently = False)

            # Email Address Confirmation Mail
            current_site = get_current_site(request)
            email_subject = "Confirm your email @ Dharma Saranam Gachhami"
            message2 = render_to_string('login/email_confirmation.html',{
                'name' : myuser.username,
                'domain' : current_site.domain,
                'uid' : urlsafe_base64_encode(force_bytes(myuser.pk)),
                'token' : generate_token.make_token(myuser)
            })
            email = EmailMessage(
                email_subject,
                message2,
                settings.EMAIL_HOST_USER,
                [myuser.email],
            )
            email.fail_silently = False
            email.send()

            return redirect('homepage')
    else:
        print(CreateUserForm.errors)
        form = CreateUserForm()

    return render(request, 'login/register.html', {'registerform': form})

# View for rendering the custom login page
def my_login(request):
    if request.user.is_authenticated:
        return render (request, 'login/index.html')

    if request.method == 'GET':
        form = LoginForm()
        return render(request,'login/my_login.html', {'loginform': form})

    elif request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            remember_me = request.POST.get('remember_me') # name must match to that of the checkbox in the template
            user = authenticate(request,username=username,password=password)

            if user is not None:
                login(request, user)


                # request.session.set_expiry(10)
                # if remember_me == 'on':
                #     settings.SESSION_EXPIRE_AT_BROWSER_CLOSE = False
                # else:
                #     settings.SESSION_EXPIRE_AT_BROWSER_CLOSE = True

                if remember_me == 'on':
                    request.session.set_expiry(604800)
                else:
                    request.session.set_expiry(0)

                
                redirect_url = reverse('homepage') + f'?username={username}'
                return redirect(redirect_url)
            
        # form is not valid or user is not authenticated
        messages.error(request, "Wrong credentials entered")
        return render(request,'login/my_login.html',{'loginform': form})

# def update_user(request):
#     if request.user.is_authenticated:
#         current_user = User.objects.get(id = request.user.id)
#         user_data, created = UserData.objects.get_or_create(user = current_user)

#         if request.method == 'POST':
#             form1 = ProfileForm(request.POST or None, instance = current_user)
#             form2 = ProfileExtraFieldsForm(request.POST, instance = user_data)
#             if form1.is_valid() and form2.is_valid():
#                 form1.save()
#                 form2.save()
#                 return redirect('update_user')
#             else:
#                 form1 = ProfileForm(request.POST or None, instance = current_user)
#                 form2 = ProfileExtraFieldsForm(request.POST, instance = user_data)
#             return render(request, 'login/update_profile.html', {'form1':form1, 'form2':form2})
        
#         else:
#             messages.error(request, "You must be logged in first!")
#             return redirect('homepage')
    
def update_user(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        user_data, created = UserData.objects.get_or_create(user=current_user)

        if request.method == 'GET':
            UserDatas = UserData.objects.all()
            return render(request, 'login/update_profile.html', {'User_Image': user_data.user_image, 'form1': ProfileForm(instance=current_user), 'form2': ProfileExtraFieldsForm(instance=user_data)})

        if request.method == 'POST':
            print(request.POST)
            form1 = ProfileForm(request.POST, request.FILES, instance=current_user)
            form2 = ProfileExtraFieldsForm(request.POST, request.FILES, instance=user_data)
            if form1.is_valid() and form2.is_valid():
                form1.save()
                form2.save()
                return redirect('update_user')
        else:
            form1 = ProfileForm(instance=current_user)
            form2 = ProfileExtraFieldsForm(instance=user_data)

        return render(request, 'login/update_profile.html', {'form1': form1, 'form2': form2})
    else:
        messages.error(request, "You must be logged in first!")
        return redirect('homepage')
    

# View for rendering the user dashboard
def dashboard(request):
    return render(request, 'login/dashboard.html')

# View for Logging Out
def my_logout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully.")
    return redirect('my_login')

def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        myuser = User.objects.get(pk = uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        myuser = None

    if myuser is not None and generate_token.check_token(myuser, token):
        myuser.is_active = True
        myuser.save()
        # login(request, myuser)
        messages.success(request, ("Verification Successful. Please log in now."))
        return redirect('my_login')
    else:
        return render(request, 'login/confirmation_fail.html')
    
# Coming-soon Page
def comingsoon(request):
    return render (request, 'login/comingsoon.html')