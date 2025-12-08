# Django 소개

## 주요 개념

### 1. Django란?
- **Python 웹 프레임워크**: 빠른 개발을 위한 고수준 프레임워크
- **MTV 패턴**: Model-Template-View (MVC의 변형)
- **배터리 포함**: 많은 기능이 내장됨
- **ORM**: 객체 관계 매핑으로 DB 조작

### 2. Django 프로젝트 구조
```
myproject/
├── manage.py
├── myproject/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── myapp/
    ├── migrations/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── tests.py
    └── views.py
```

### 3. MTV 패턴
- **Model**: 데이터베이스 스키마
- **Template**: HTML 템플릿
- **View**: 비즈니스 로직

### 4. 기본 명령어
```bash
# 프로젝트 생성
django-admin startproject myproject

# 앱 생성
python manage.py startapp myapp

# 서버 실행
python manage.py runserver

# 마이그레이션
python manage.py makemigrations
python manage.py migrate
```

## 예시 코드

### settings.py 설정
```python
# myproject/settings.py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapp',  # 생성한 앱 추가
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

### urls.py - URL 설정
```python
# myproject/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
]
```

### views.py - 뷰 작성
```python
# myapp/views.py
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("Hello, Django!")

def home(request):
    context = {
        'message': 'Welcome to Django'
    }
    return render(request, 'home.html', context)
```

## 기본 코드 템플릿

### 프로젝트 시작
```bash
# 가상환경 생성 및 활성화
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Django 설치
pip install django

# 프로젝트 생성
django-admin startproject myproject
cd myproject

# 앱 생성
python manage.py startapp myapp

# 서버 실행
python manage.py runserver
```

## 연습 파일
- Django 프로젝트 생성
- 앱 생성 및 설정
- 기본 뷰 작성
