from django import forms
from carsapp.models import Car


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'
