from django import forms
from .models import Menu


class MenuForm(forms.ModelForm):
    # price: 자리수/형식 검증 + 커스텀 에러메시지
    price = forms.DecimalField(
        max_digits=8,
        decimal_places=2,
        error_messages={
            'invalid': "올바른 가격을 입력해 주세요. 예: '12.34'",
            'max_digits': "가격은 최대 8자리여야 합니다.",
            'max_decimal_places': "가격은 소수점 이하 두 자리여야 합니다.",
            # (선택) 정수부 초과 시
            'max_whole_digits': "가격의 정수부가 너무 깁니다.",
        },
    )

    # is_vegan: RadioSelect (Yes/No 노출, True/False 저장)
    is_vegan = forms.TypedChoiceField(
        choices=((True, 'Yes'), (False, 'No')),
        coerce=lambda v: v == 'True',
        widget=forms.RadioSelect,
        label='Is vegan',
    )
    class Meta:
        model = Menu
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '메뉴 이름을 작성해 주세요.'
                    }
                ),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': '메뉴 설명을 작성해 주세요.'
                    }
                ),
            'is_vegan': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'price': forms.TextInput(attrs={'class': 'form-control'}),
        }