from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=12,
        label='Username',
        widget=forms.TextInput(attrs={
            'maxlength' : '12',
        }))
    password = forms.CharField(
        label = 'Password',
        widget=forms.PasswordInput()
    )