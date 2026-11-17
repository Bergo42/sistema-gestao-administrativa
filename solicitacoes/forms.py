from django import forms
from .models import Solicitacao


class SolicitacaoForm(forms.ModelForm):
    class Meta:
        model = Solicitacao
        fields = ['cliente', 'descricao', 'prazo', 'status']

        widgets = {
            'cliente': forms.Select(attrs={
                'class': 'form-select'
            }),
            'descricao': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Descreva o serviço solicitado'
            }),
            'prazo': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'status': forms.Select(attrs={
                'class': 'form-select'
            }),
        }