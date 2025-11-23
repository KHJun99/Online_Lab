from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, CustomUserChangeForm
# from .forms import LoginForm


User = get_user_model()

# Create your views here.
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('todos:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)

def logout(request):
    auth_logout(request)
    return redirect('accounts:login')

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('todos:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/signup.html', context)

@login_required
def delete(request):
    request.user.delete()
    auth_logout(request)
    return redirect('accounts:login')

@login_required
def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('todos:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form': form
    }
    return render(request, 'accounts/update.html', context)

def change_password(request, user_pk):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            return redirect('todos:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form': form
    }
    return render(request, 'accounts/change_password.html', context)

def profile(request, username):
    profile_owner = get_object_or_404(User, username=username)
    like_diaries = profile_owner.diary_set.all()
    
    # 구독자 수와 구독 중인 수 계산
    followers_count = profile_owner.followers.count()  # 나를 구독하는 사람 수
    followings_count = profile_owner.followings.count()  # 내가 구독하는 사람 수
    
    context = {
        'profile_owner': profile_owner,
        'like_diaries': like_diaries,
        'followers_count': followers_count,
        'followings_count': followings_count,
    }
    return render(request, 'accounts/profile.html', context)

@login_required
def subscribe(request, user_pk):
    # 구독 대상 유저
    target_user = get_object_or_404(User, pk=user_pk)
    
    # 자기 자신은 구독할 수 없음
    if request.user == target_user:
        return redirect('accounts:profile', username=target_user.username)
    
    # 이미 구독 중이면 구독 취소, 아니면 구독
    if target_user.followers.filter(pk=request.user.pk).exists():
        # 구독 취소
        target_user.followers.remove(request.user)
    else:
        # 구독
        target_user.followers.add(request.user)
    
    return redirect('accounts:profile', username=target_user.username)