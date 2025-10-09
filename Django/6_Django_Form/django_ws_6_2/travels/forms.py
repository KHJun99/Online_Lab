from django import forms
from .models import Travels

class TravelForm(forms.ModelForm):
    class Meta:
        model = Travels
        fields = ['location', 'plan', 'start_date', 'end_date']
        widgets = {
            'location' : forms.TextInput(attrs={'placeholder' : 'ex) 제주도'}),
            'plan' : forms.Textarea(attrs={'placeholder' : '슉. 슈슉.'}),
            'start_date' : forms.DateInput(attrs={'placeholder' : 'ex)2022-02-22'}),
            'end_date' : forms.DateInput(attrs={'placeholder' : 'ex)2022-02-22'}),
        }