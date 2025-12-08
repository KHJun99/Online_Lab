# Django Templates

## 주요 개념

### 1. 템플릿이란?
- **HTML 파일**: 동적 콘텐츠를 포함한 HTML
- **템플릿 언어**: Django Template Language (DTL)
- **변수**: `{{ variable }}`
- **태그**: `{% tag %}`
- **필터**: `{{ value|filter }}`

### 2. 템플릿 위치
```
myapp/
└── templates/
    └── myapp/
        └── index.html
```

### 3. DTL 문법
- **변수 출력**: `{{ variable }}`
- **조건문**: `{% if %} ... {% endif %}`
- **반복문**: `{% for %} ... {% endfor %}`
- **상속**: `{% extends %}`, `{% block %}`

## 예시 코드

### 기본 템플릿
```html
<!-- templates/myapp/index.html -->
<!DOCTYPE html>
<html>
<head>
    <title>{{ title }}</title>
</head>
<body>
    <h1>{{ message }}</h1>

    {% if user_name %}
        <p>안녕하세요, {{ user_name }}님!</p>
    {% else %}
        <p>로그인하세요</p>
    {% endif %}

    <ul>
    {% for item in items %}
        <li>{{ item }}</li>
    {% endfor %}
    </ul>
</body>
</html>
```

### 템플릿 상속
```html
<!-- templates/base.html -->
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}My Site{% endblock %}</title>
</head>
<body>
    <header>
        <h1>My Website</h1>
    </header>

    <main>
        {% block content %}
        {% endblock %}
    </main>

    <footer>
        <p>&copy; 2024</p>
    </footer>
</body>
</html>
```

```html
<!-- templates/myapp/page.html -->
{% extends 'base.html' %}

{% block title %}페이지 제목{% endblock %}

{% block content %}
    <h2>페이지 내용</h2>
    <p>{{ content }}</p>
{% endblock %}
```

### 필터 사용
```html
<p>{{ text|lower }}</p>  <!-- 소문자 변환 -->
<p>{{ text|upper }}</p>  <!-- 대문자 변환 -->
<p>{{ text|title }}</p>  <!-- 제목 형식 -->
<p>{{ value|default:"기본값" }}</p>  <!-- 기본값 -->
<p>{{ my_date|date:"Y-m-d" }}</p>  <!-- 날짜 포맷 -->
<p>{{ number|add:5 }}</p>  <!-- 덧셈 -->
<p>{{ text|length }}</p>  <!-- 길이 -->
```

### View에서 템플릿 사용
```python
# views.py
from django.shortcuts import render

def index(request):
    context = {
        'title': '홈페이지',
        'message': '환영합니다',
        'user_name': '홍길동',
        'items': ['Apple', 'Banana', 'Cherry']
    }
    return render(request, 'myapp/index.html', context)
```

## 기본 코드 템플릿

### base.html (기본 레이아웃)
```html
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}My Site{% endblock %}</title>
    {% block extra_css %}{% endblock %}
</head>
<body>
    <nav>
        <a href="{% url 'home' %}">홈</a>
        <a href="{% url 'about' %}">소개</a>
    </nav>

    {% block content %}
    {% endblock %}

    {% block extra_js %}{% endblock %}
</body>
</html>
```

### 자식 템플릿
```html
{% extends 'base.html' %}

{% block title %}페이지 제목{% endblock %}

{% block content %}
    <h1>{{ title }}</h1>

    {% for item in items %}
        <div>
            <h3>{{ item.title }}</h3>
            <p>{{ item.content|truncatewords:30 }}</p>
        </div>
    {% empty %}
        <p>항목이 없습니다.</p>
    {% endfor %}
{% endblock %}
```

## 연습 파일
- DTL 문법 활용
- 템플릿 상속
- 필터 사용
