from django import forms
from .models import Jenerator

class AddProductForm(forms.ModelForm):
    class Meta:
        model = Jenerator
        fields = '__all__'
