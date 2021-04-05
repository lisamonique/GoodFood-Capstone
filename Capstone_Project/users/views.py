from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def register(request):

    if request.method == 'GET':
        error = request.GET.get("error", "")
        username = request.GET.get("username", "")
        email = request.GET.get("email", "")

        context = {
            'error': error,
            'username': username,
            'email': email
        }
        return render(request, 'users/register.html', context)

    elif request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        confirm = request.POST['confirm']
        email = request.POST['email']
        
        if password == confirm:
            User.objects.create_user(username, email, password)
            return HttpResponseRedirect(reverse('login_user'))
        else:
            return HttpResponseRedirect(reverse('register') + f'?error=passwords do not match&username={username}&email={email}')


def login_user(request):
    
    if request.method == "GET":
        error = request.GET.get('error', '')
        context = {
            'error': error
        }
        return render(request, 'users/login.html', context)
    
    elif request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('profile'))
        else:
            return HttpResponseRedirect(reverse('login_user') + '?error=Username or Password is incorrect.')

def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('plants:index'))

@login_required
def profile(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login_user'))

    return render(request, 'users/profile.html')