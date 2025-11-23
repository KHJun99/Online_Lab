from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model
from .forms import CustomUserCreationForm, CustomUserChangeForm, CustomUserIsStaffForm

User = get_user_model()
# Create your views here.
def index(request):
    members = User.objects.all()
    context = {
        'members': members
    }
    return render(request, 'accounts/index.html', context)

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('stores:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)

def logout(request):
    if request.method == 'POST':
        auth_logout(request)
    return redirect('accounts:login')


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('stores:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)

def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('accounts:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/update.html', context)

def is_staff_update(request, user_pk):
    user = User.objects.get(pk=user_pk)
    if request.user.is_superuser:
        if request.method == "POST":
            form = CustomUserIsStaffForm(request.POST, instance=user)
            if form.is_valid():
                form.save()
                return redirect('accounts:index')
        else:
            form = CustomUserIsStaffForm(instance=user)
        context = {
            'form' : form
        }
        return render(request, 'accounts/is_staff_update.html', context)
    
def delete(request, user_pk):
    user = User.objects.get(pk=user_pk)
    if request.user.is_superuser:
        if request.method == "POST":
            user.delete()
    return redirect('accounts:index')