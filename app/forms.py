from django import forms
from .models import Cliente # type: ignore

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'email', 'senha']
        widgets = {
            'senha': forms.PasswordInput()  # Para que o campo de senha seja mascarado
        }
