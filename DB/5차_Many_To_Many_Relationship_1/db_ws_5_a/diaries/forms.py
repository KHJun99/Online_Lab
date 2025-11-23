from django import forms
from .models import Diary, Comment


class DiaryForm(forms.ModelForm):

    class Meta:
        model = Diary
        fields = ['content', 'picture']
        widgets = {
            'content' : forms.Textarea(attrs={'placeholder' : '오늘의 일기를 작성하세요'})
        }

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        # fields = ('content',)
        exclude = ('diary',)