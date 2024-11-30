from django import forms
from .models import Sponsers


class SponsersForm(forms.ModelForm):

    class Meta:
        model = Sponsers
        fields = '__all__'