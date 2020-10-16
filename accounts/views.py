from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

def register_user(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            username =request.POST['username']
            email =request.POST['email']
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
