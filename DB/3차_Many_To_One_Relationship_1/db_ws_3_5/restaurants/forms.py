from django import forms
from .models import Restaurant, Menu


class RestaurantForm(forms.ModelForm):
    
    class Meta:
        model = Restaurant
        fields = '__all__'
        widgets = {
            'category': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'descriptions': forms.Textarea(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'opening_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'closing_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
        }

class MenuForm(forms.ModelForm):
    
    class Meta:
        model = Menu
        exclude = ('restaurant', )
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'is_vegan': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class MenuUpdateForm(forms.ModelForm):

    class Meta:
        model = Menu
        exclude = ('restaurant', 'name',)
        widgets = {
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'is_vegan': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }