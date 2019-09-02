from django import forms
from exames.models import Exame

class ExameCreateForm(forms.ModelForm):
    class Meta:
        model = Exame
        fields = ['texto','medico','paciente']  
        # lembrar de MODIFICAR CARAMBA
    
    