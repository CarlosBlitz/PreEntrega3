from django import forms

class turnoFormulario(forms.Form):
    prestador = forms.CharField()
    solicitante = forms.CharField()
    fecha = forms.DateField()