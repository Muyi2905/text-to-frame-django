from django import forms
from .models import ImageText

class ImageTextForm(forms.ModelForm):
    class Meta:
        model = ImageText
        fields = ['image', 'text']
