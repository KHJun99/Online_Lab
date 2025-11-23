from django import forms
from .models import Author, Book


class AuthorForm(forms.ModelForm):

    class Meta:
        model = Author
        fields = ('nickname', )


class BookForm(forms.ModelForm):
    
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 해당 user가 가진 작가명만 선택 가능하도록 필터링
        self.fields['author'].queryset = Author.objects.filter(user=user)
    
    class Meta:
        model = Book
        fields = '__all__'