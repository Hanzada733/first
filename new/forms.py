from django import forms
from new.models import *
class OrderForm(forms.ModelForm):
    favorite_fruit = forms.CharField(label='What is your favorite fruit?',
                                     widget=forms.RadioSelect())
    class Meta:
        model=Order
        exclude=['sait','brand','marketing']

