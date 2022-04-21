from django import forms
from Airportdetail.models import Data


class DatainputForm(forms.ModelForm):
    class Meta:
        model=Data
        fields = ["jsonfile"]