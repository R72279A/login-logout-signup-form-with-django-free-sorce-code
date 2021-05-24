from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User

# Create your views here.


def home(request):
    return render(request, "home.html")


def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if username == password1:
            messages.error(request, "you can't set your name as your password")
            return redirect('/')

        if password1 != password2:
            messages.error(request,"your Password does not match")
            return redirect('/')

        my_user = User.objects.create_user(username, email, password1)
        my_user.save()
        messages.success(request, "Signup Successful")
        return redirect('/')

    return render(request, 'signup.html')


def login(request):
    if request.method == 'POST':
        loginusername = request.POST.get('loginusername')
        loginpassword = request.POST.get('loginpassword')

        user = authenticate(username=loginusername, password=loginpassword)

        if user is not None:
            auth_login(request, user)
            messages.success(request, 'Login Sucessful')
            return redirect('/')
        else:
            messages.error(request, 'No Such User, Please Try Again.')
            return redirect('/')

    return render(request, 'login.html')

def logout(request):
    auth_logout(request)
    messages.error(request, 'Logout Successful')
    return redirect('/')