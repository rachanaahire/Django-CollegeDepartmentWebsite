from django import forms
from .models import list


class ListForm(forms.ModelForm):
    class Meta:
        model = list
        fields = ["item","completed"]


