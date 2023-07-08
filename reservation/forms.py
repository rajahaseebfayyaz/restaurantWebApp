from django import forms
from django.forms import fields
from .models import Reservation , TokenModle

class ReserveTableForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = '__all__'

class TokenForm(forms.ModelForm):
    class Meta:
        model = TokenModle
        fields = '__all__'
