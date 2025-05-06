from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages 
from django.contrib.auth.decorators import login_required
# Create your views here.
def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('signup')

        user=User.objects.create_user(username=username, password=password)
        user.save()
        messages.success(request, "Account created successfully!")
        return redirect('login')

    return render(request, 'bank/signup.html')
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username') 
        password = request.POST.get('password') 
        user = authenticate(request, username=username, password=password)
     
        if user is not None:
            login(request, user)
            return redirect('dashboard') 
        else:
            messages.error(request, "Invalid credentials")
    
    # This should be outside POST block
    return render(request, 'bank/login.html')
@login_required
def dashboard(request):
    return render(request, 'bank/dashboard.html')

def study(request):
    return render(request, 'bank/study.html')

def expert(request):
    return render(request, 'bank/expert.html')
def motivation(request):
    return render(request, 'bank/motivation.html')

def CBSE10(request):
    return render(request, 'bank/CBSE10.html')

def CBSE12(request):
    return render(request, 'bank/CBSE12.html')

def PSEB10(request):
    return render(request, 'bank/PSEB10.html')

def PSEB12(request):
    return render(request, 'bank/PSEB12.html')

def material110(request):
    return render(request, 'bank/material110.html')

def material210(request):
    return render(request, 'bank/material210.html')

def material310(request):
    return render(request, 'bank/material310.html')

def material410(request):
    return render(request, 'bank/material410.html')

def material510(request):
    return render(request, 'bank/material510.html')

def material610(request):
    return render(request, 'bank/material610.html')

def material710(request):
    return render(request, 'bank/material710.html')

def material810(request):
    return render(request, 'bank/material810.html')

def material910(request):
    return render(request, 'bank/material910.html')

def material1010(request):
    return render(request, 'bank/material1010.html')


def material1112(request):
    return render(request, 'bank/material1112.html')

def material1212(request):
    return render(request, 'bank/material1212.html')

def material1312(request):
    return render(request, 'bank/material1312.html')

def material1412(request):
    return render(request, 'bank/material1412.html')

def material1512(request):
    return render(request, 'bank/material1512.html')

def material1612(request):
    return render(request, 'bank/material1612.html')

def material1712(request):
    return render(request, 'bank/material1712.html')

def material1812(request):
    return render(request, 'bank/material1812.html')

def material1912(request):
    return render(request, 'bank/material1912.html')

def material2012(request):
    return render(request, 'bank/material2012.html')

def material2110(request):
    return render(request, 'bank/material2110.html')

def material2210(request):
    return render(request, 'bank/material2210.html')

def material2310(request):
    return render(request, 'bank/material2310.html')


def material2410(request):
    return render(request, 'bank/material2410.html')

def material2510(request):
    return render(request, 'bank/material2510.html')

def material2610(request):
    return render(request, 'bank/material2610.html')

def material2710(request):
    return render(request, 'bank/material2710.html')

def material2810(request):
    return render(request, 'bank/material2810.html')

def material2912(request):
    return render(request, 'bank/material2912.html')

def material3012(request):
    return render(request, 'bank/material3012.html')

def material3112(request):
    return render(request, 'bank/material3112.html')

def material3212(request):
    return render(request, 'bank/material3212.html')

def material3312(request):
    return render(request, 'bank/material3312.html')

def material3412(request):
    return render(request, 'bank/material3412.html')


def material3512(request):
    return render(request, 'bank/material3512.html')

def material3612(request):
    return render(request, 'bank/material3612.html')

def logout_view(request):
    logout(request)
    return redirect('login')