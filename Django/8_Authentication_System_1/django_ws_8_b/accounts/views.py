from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.views.decorators.http import require_http_methods


# Create your views here.
@require_http_methods(["GET", "POST"])
def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'todos:index')
    else:
        form = AuthenticationForm(request)
    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)


@require_http_methods(["POST"])
def logout(request):
    auth_logout(request)
    return redirect('todos:index')