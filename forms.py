from django import forms
from .models import menmodel

class menform(forms.ModelForm):
    class Meta:
        model = menmodel
        fields = '__all__'