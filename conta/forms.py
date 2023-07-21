from django.contrib.auth.forms import UserCreationForm
from .models import Usuario, FuturasCompra
from django import forms

class CriarContaForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = Usuario
        fields = ('username', 'email', 'password1','password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Usuario.objects.filter(email=email).exists():
            raise forms.ValidationError("Este email já esta em uso. Por favor, escolha outro")
        return email


class FuturasCompras(forms.ModelForm):
    class Meta:
        model = FuturasCompra
        fields=['descricao', 'valor', 'url', 'usuario']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        self.fields['descricao'].widget.attrs.update({'placeholder': 'Insira aqui o nome do produto'})
        self.fields['valor'].widget.attrs.update({'placeholder': 'Insira aqui o valor do produto'})
        self.fields['url'].widget.attrs.update({'placeholder': 'Insira aqui o link do produto'})
        self.fields['descricao'].label = 'Produto'
        self.fields['valor'].label = 'Valor'
        self.fields['url'].label = 'Link'
        if self.user:
            self.fields['usuario'].widget = forms.HiddenInput()
            self.fields['usuario'].initial = self.user
            self.fields['usuario'].required = False


    def save(self, commit=True):
        instance = super().save(commit=False)
        if self.user:
            instance.usuario = self.user
        if commit:
            instance.save()
        return instance








