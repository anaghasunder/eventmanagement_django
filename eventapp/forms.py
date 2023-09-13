from django import forms
from .models import Eventdetail

class Applicantform(forms.ModelForm):
    class Meta:
        model = Eventdetail
        fields = ['name','email','phone']
