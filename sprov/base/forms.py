from django import forms
from .models import CustomersModel


class ConsultingForm(forms.ModelForm):
    class Meta:
        model = CustomersModel
        fields = '__all__'
