from django import forms

from .models import Guest


class GuestForm(forms.ModelForm):
    
    class Meta:
        model = Guest
        fields = ['first_name', 'last_name', 'adult_guest', 'child_guest', 'whatsapp']