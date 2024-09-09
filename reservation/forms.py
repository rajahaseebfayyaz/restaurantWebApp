from django import forms
from django.forms import fields
from .models import Reservation , TokenModle
from django.contrib.auth.models import User

class ReserveTableForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['number_of_persons', 'date', 'time']
        # fields = '__all__'

class TokenForm(forms.ModelForm):
    class Meta:
        model = TokenModle
        fields = '__all__'
