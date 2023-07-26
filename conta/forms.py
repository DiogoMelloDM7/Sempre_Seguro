from django.contrib.auth.forms import UserCreationForm
from .models import Usuario, FuturasCompra, ContasAVencer
from django import forms

class CriarContaForm(UserCreationForm):
    email = forms.EmailField()
    telefone = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder': 'Exemplo: +55 (11) 9 1234-5678'}))

    class Meta:
        model = Usuario
        fields = ('username', 'email','telefone', 'password1','password2')

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


class ContasAVencerem(forms.ModelForm):

    class Meta:
        model = ContasAVencer
        fields = ['usuario', 'descricao', 'valor', 'data_vencimento']

        widgets = {
            'data_vencimento': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):

        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        self.fields['descricao'].widget.attrs.update({'placeholder': 'Insira aqui a descrição da conta'})
        self.fields['valor'].widget.attrs.update({'placeholder': 'Insira aqui o valor da conta: '})
        self.fields['descricao'].label = 'Descrição da conta'
        self.fields['valor'].label = 'Valor da conta'
        self.fields['data_vencimento'].label = 'Data de Vencimento'
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







