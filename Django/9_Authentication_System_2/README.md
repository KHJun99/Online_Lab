# Django Authentication System (2)

## 주요 개념

### 1. 로그인 필수 데코레이터
- `@login_required`: 로그인 필수 View
- 미로그인 시 로그인 페이지로 리다이렉트

### 2. 사용자 정보 접근
- `request.user`: 현재 사용자
- `request.user.is_authenticated`: 로그인 여부
- `request.user.username`: 사용자명

### 3. 비밀번호 변경
- `PasswordChangeForm`: 비밀번호 변경 폼
- `update_session_auth_hash()`: 세션 유지

## 예시 코드

### 로그인 필수 View
```python
from django.contrib.auth.decorators import login_required

@login_required
def profile_view(request):
    return render(request, 'profile.html')
```

### 사용자 정보 표시
```html
{% if request.user.is_authenticated %}
    <p>안녕하세요, {{ request.user.username }}님!</p>
    <a href="{% url 'logout' %}">로그아웃</a>
{% else %}
    <a href="{% url 'login' %}">로그인</a>
{% endif %}
```

### 비밀번호 변경
```python
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('profile')
    else:
        form = PasswordChangeForm(request.user)

    return render(request, 'change_password.html', {'form': form})
```

## 기본 코드 템플릿

### 인증 관련 View
```python
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

@login_required
def profile(request):
    return render(request, 'profile.html')

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('profile')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {'form': form})
```
