# Django Form

## 주요 개념

### 1. Django Form
- **폼 클래스**: Python 클래스로 폼 정의
- **유효성 검사**: 자동 검증
- **위젯**: 입력 필드 렌더링
- **CSRF**: 보안 토큰

### 2. ModelForm
- **모델 기반**: 모델에서 자동 생성
- **간편한 저장**: `form.save()`

## 예시 코드

### Form 클래스
```python
# forms.py
from django import forms

class ArticleForm(forms.Form):
    title = forms.CharField(max_length=200)
    content = forms.CharField(widget=forms.Textarea)
```

### ModelForm
```python
from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content']
        # fields = '__all__'  # 모든 필드
```

### View에서 Form 사용
```python
def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('article_detail', article.pk)
    else:
        form = ArticleForm()

    return render(request, 'create.html', {'form': form})
```

### 템플릿에서 Form 렌더링
```html
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">제출</button>
</form>
```

## 기본 코드 템플릿

### ModelForm 기본
```python
# forms.py
from django import forms
from .models import MyModel

class MyModelForm(forms.ModelForm):
    class Meta:
        model = MyModel
        fields = '__all__'
        widgets = {
            'field': forms.Textarea(attrs={'rows': 5})
        }
```

### Create View with Form
```python
def create_view(request):
    if request.method == 'POST':
        form = MyModelForm(request.POST)
        if form.is_valid():
            instance = form.save()
            return redirect('detail', instance.pk)
    else:
        form = MyModelForm()

    return render(request, 'create.html', {'form': form})
```
