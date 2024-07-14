# accounts/views.py
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


def welcome(request):
    return render(request, 'welcome.html')


def register(request):
    if request.method == 'POST':
        print(request.POST)
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            # Replace 'home' with your desired redirect URL after registration
            return redirect('profile')
    else:
        form = SignUpForm()
    return render(request, 'registration/register.html', {'form': form})

# register/views.py


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page or home page
            # Replace 'home' with your desired URL name
            return redirect('profile')
        else:
            # Return an 'invalid login' error message
            messages.error(request, 'Invalid username or password.')
    return render(request, 'registration/login.html')


@login_required
def user_info(request):
    # *Route Params
    return render(request, 'user_info.html', {'user': request.user})

# myapp/views.py

# ? Query Params


def search_books(request):
    title = request.GET.get('title', '')
    author = request.GET.get('author', '')

    return HttpResponse(f"Searching books - Title: {title}, Author: {author}")


def test(request, username):
    return render(request, 'welcome.html', {'username': username})


def practice(request):
    return HttpResponse("Hello, World!"+__file__)


def profile(request):
    return HttpResponse("Hello, World!"+__file__)
