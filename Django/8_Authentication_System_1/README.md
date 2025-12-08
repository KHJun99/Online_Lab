# Django Authentication System (1)

## 주요 개념

### 1. 인증 시스템
- **User 모델**: 기본 제공
- **로그인/로그아웃**: 인증 처리
- **회원가입**: 사용자 생성
- **비밀번호 관리**: 해시 처리

### 2. 주요 함수
- `login()`: 로그인
- `logout()`: 로그아웃
- `authenticate()`: 인증 확인
- `UserCreationForm`: 회원가입 폼

## 예시 코드

### 로그인
```python
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})
```

### 로그아웃
```python
from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return redirect('home')
```

### 회원가입
```python
from django.contrib.auth.forms import UserCreationForm

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()

    return render(request, 'signup.html', {'form': form})
```

## 기본 코드 템플릿

### 인증 관련 View
```python
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('home')

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
```
