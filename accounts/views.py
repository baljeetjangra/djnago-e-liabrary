from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages


def register_user(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            username =request.POST['username']
            email =request.POST['email']
            user_type = request.POST['user_type']
            password1 =request.POST['password1']
            password2 =request.POST['password2']

            if password1 == password2:
                if User.objects.filter(username=username).exists():
                    messages.info(request, "Username is already exists !")
                elif User.objects.filter(email=email).exists():
                    messages.info(request, 'Email is already exists !')
                    return redirect('Accounts:register_user')
                else:
                    user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                    user.save()
                    return redirect('/')
            else:
                messages.info(request, "Password didn't match !")
                return redirect('Accounts:register_user') 
        return render(request, 'accounts/register.html')


def login_user(request):
    if not request.user.is_authenticated:
        if request.method =='POST':
            username = request.POST['username']
            password = request.POST['password']

            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('/')
            else:
                messages.info(request, 'invalid credential!')
                return redirect('Accounts:login_user')
        else:
            return render(request, 'accounts/login.html')
    return redirect('/')

def logout_user(request):
    auth.logout(request)
    return redirect("Accounts:login_user")