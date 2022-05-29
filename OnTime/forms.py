from django import forms
from .models import *

class DateInput(forms.DateInput):
    input_type = 'date'

class profform(forms.ModelForm):
    class Meta:
        model = person
        fields = '__all__'
        widgets = {
            'date': DateInput()
        }

    def __init__(self, *args, **kwargs):
        super(profform, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['date'].widget.attrs['class'] = 'form-control'
        self.fields['phone'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['rating'].widget.attrs['class'] = 'form-control'
        self.fields['profession'].widget.attrs['class'] = 'form-control'

