from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid login credentials!')
            return redirect('login')

    return render(request, 'accounts/login.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        user_name = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=user_name).exists():
                messages.error(request, "Username already exists! Please, Log In")
                return redirect('register')
            else:
                if User.objects.filter(email=email):
                    messages.error(request, 'Email already exists!')
                    return redirect('register')
                else:
                    user = User.objects.create_user(
                        first_name=first_name,
                        last_name=last_name,
                        username=user_name,
                        email=email,
                        password=password
                    )
                    auth.login(request, user)
                    messages.success(request, 'You are now logged in!')
                    return redirect('dashboard')
                    # user.save() This for redirecting to login (if we don't want auto redirecting user to dashboard)
                    # messages.success(request, "You are registered successfully!")

                return redirect('login')
        else:
            messages.error(request, "Passwords do not match!")
            return redirect('register')
    return render(request, 'accounts/register.html')


def dashboard(request):
    return render(request, 'accounts/dashboard.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are successfully logged out!')
        return redirect('home')
    return redirect('home')
