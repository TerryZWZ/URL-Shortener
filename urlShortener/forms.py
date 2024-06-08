from .models import ShortURL
from django import forms

# Creating Form
class CreateNewShortURL(forms.ModelForm):
    class Meta:
        model = ShortURL
        fields = { 'Original_URL' }
        labels = { 'Original_URL': '' }

        widgets = { 
            'Original_URL' : forms.TextInput(attrs = { 
                'class' : 'formControl',
                'style': '-webkit-text-fill-color: #003E5A; -webkit-box-shadow: 0 0 0px 40rem #33C1FF inset;'})
        }