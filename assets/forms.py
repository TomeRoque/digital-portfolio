from django import forms
from django.forms import ModelForm
from .models import Portfolio


class PortfolioForm(ModelForm):
    class Meta:
        model = Portfolio
        fields = '__all__'
        # inserção de classes CSS para formatação de cada campo do formulário
        widgets = {
            'nome': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Insira o nome a aparecer como autor...'}),
            'comentario': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Escreva aqui o seu comentário...'}),
        }

        # texto a exibir junto à janela de inserção
        labels = {
            'nome': 'Nome',
            'comentario': 'Comentario',
        }

        # texto auxiliar a um determinado campo do formulário
        help_texts = {
            'nome': 'Escreva "Anónimo" caso não queira deixar o seu nome',
        }
