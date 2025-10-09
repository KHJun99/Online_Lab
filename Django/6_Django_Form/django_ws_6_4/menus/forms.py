from django import forms
from .models import Menu

# ... 생략 ...
class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ['name', 'price', 'description', 'is_vegan']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '메뉴 이름을 작성해 주세요.'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 7, 'placeholder': '메뉴 설명을 작성해 주세요.'}),
            # ✅ form-check-input 제거
            'is_vegan': forms.CheckboxInput(attrs={'id': 'id_is_vegan'}),
        }

