# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.views.decorators.http import require_http_methods, require_POST

User = get_user_model()

@require_http_methods(["GET"])
def index(request):
    users = User.objects.all().order_by('username')
    return render(request, 'accounts/index.html', {'users': users})

@require_http_methods(["GET", "POST"])
def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)  
        if form.is_valid():
            auth_login(request, form.get_user())
   
            return redirect('accounts:index')
    else:
        form = AuthenticationForm(request)
    return render(request, 'accounts/login.html', {'form': form})

@require_POST
def logout(request):
    auth_logout(request)
    return redirect('accounts:index')
