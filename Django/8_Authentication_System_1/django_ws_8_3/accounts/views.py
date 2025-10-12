from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from .models import User
from django.db.models import F

# Create your views here.
def index(request):
    persons = User.objects.all().order_by('-score', 'id')
    context = {
        'persons': persons
    }
    return render(request, 'accounts/index.html', context)

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('accounts:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)

def logout(request):
    auth_logout(request)
    return redirect('accounts:index')


def add_score(request, user_pk):
    if request.method == "POST":
        target = get_object_or_404(User, pk=user_pk)
        target.score = F('score') + 100
        target.save(update_fields=['score'])
        
        target.refresh_from_db(fields=['score'])
    return redirect('accounts:index')