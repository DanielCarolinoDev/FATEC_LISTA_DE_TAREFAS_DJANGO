from .models import AtividadeModel
from django.forms import ModelForm
from django import forms
from datetime import date

class AtividadeModelForm(ModelForm):
    class Meta:
        model = AtividadeModel
        fields = ['id','titulo','data','local','tarefa']


class DataForm(forms.Form):
    hoje = forms.DateField(initial=date.today)