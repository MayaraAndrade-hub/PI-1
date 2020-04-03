from django import forms  
from equipamento.models import Equipamento  
class EquipamentoForm(forms.ModelForm):  
    class Meta:  
        model = Equipamento  
        fields = "__all__"  