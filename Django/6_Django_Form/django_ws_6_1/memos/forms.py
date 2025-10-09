from django import forms
from .models import Memo

class MemoForm(forms.ModelForm):
    class Meta:
        model = Memo
        fields = ['summary', 'memo']
        widgets = {
            'summary': forms.TextInput(attrs={'placeholder': 'summary'}),
            # textarea 크기는 rows/cols로!
            'memo': forms.Textarea(attrs={'placeholder': 'memo', 'rows': 5, 'cols': 50}),
        }
