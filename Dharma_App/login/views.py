from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def homepage(request):
    return render(request, 'login/index.html')

def register(request):
    return render(request, 'login/register.html')

def my_login(request):
    return render(request, 'login/my_login.html')

def dashboard(request):
    return render(request, 'login/dashboard.html')