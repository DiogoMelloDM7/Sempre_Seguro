from django.views.generic import TemplateView, ListView, DetailView, FormView, UpdateView, View
from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import FuturasCompra, Relatorio, Usuario, Conta, Recebimento, ContasAVencer, ContasInformada
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CriarContaForm, FuturasCompras, ContasAVencerem
from django.http import JsonResponse
from django.core.mail import send_mail
from datetime import date


def enviar_email_vencimento_contas():

    hoje = date.today()
    contas_a_vencer_hoje = ContasAVencer.objects.filter(data_vencimento=hoje)
    for conta in contas_a_vencer_hoje:
        conta_informada_existente = ContasInformada.objects.filter(usuario=conta.usuario, descricao=conta.descricao, valor=conta.valor, data_vencimento=conta.data_vencimento).exists()
        if not conta_informada_existente:
            email_usuario = conta.usuario.email

            assunto = f"Conta a vencer: {conta.descricao}"
            mensagem = f"Olá {conta.usuario.username},\n \nVocê possui uma conta pendente com o vencimento para hoje referente a {conta.descricao} no valor de {conta.valor}!!! \n \nAtenciosamente, \n \nSempre Seguro."

            send_mail(assunto, mensagem, 'grilodobone@hotmail.com', [email_usuario])
            conta_informada = ContasInformada(usuario=conta.usuario, descricao=conta.descricao, valor=conta.valor, data_vencimento=conta.data_vencimento)
            conta_informada.save()



class Homepage(TemplateView):
    template_name = 'homepage.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            try:
                dicionarioItemDespesas(request)
                dicionarioItemRecebimentos(request)
                #enviar_email_vencimento_contas()
                return redirect('conta:homepagelogin')
            except:
                #enviar_email_vencimento_contas()
                return redirect('conta:homepagelogin')
        else:
            return super().get(request, *args, **kwargs)


class CriarConta(FormView):
    template_name = 'criarconta.html'
    form_class = CriarContaForm

    def get_success_url(self):
        return reverse('conta:login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class FuturasCompras(LoginRequiredMixin, FormView):
    template_name = 'futurascompras.html'
    form_class = FuturasCompras

    def get_success_url(self):
        return reverse('conta:futurascompras')

    def get(self, request):
        try:
            form = self.form_class(user=request.user)
            return render(request, self.template_name, {'form':form})
        except:
            return redirect('conta:error')

    def post(self, request):
        form = self.form_class(request.POST, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('conta:futurascompras')
        return render(request, self.template_name, {'form':form})

class HomepageLogin(LoginRequiredMixin, TemplateView):
    template_name = 'homepagelogin.html'



class Saldo(LoginRequiredMixin, DetailView):

    template_name = 'saldo.html'
    model = Relatorio

    def get(self, request, *args, **kwargs):
        try:
            return super().get(request, *args, **kwargs)
        except:
            return redirect('conta:error')


class Relatorios(LoginRequiredMixin, ListView):
    template_name = 'relatorios.html'
    model = Relatorio



class EditarPerfil(LoginRequiredMixin, UpdateView):
    template_name = 'editarperfil.html'
    model = Usuario
    fields = ['first_name', 'last_name', 'email', 'username', 'telefone']

    def get_success_url(self):
        return reverse('conta:homepagelogin')

lista_geral_despesas = {}
lista_despesas = []
def despesas(request):
    try:
        if request.user not in lista_geral_despesas:
            listaVaziaDespesas()
        if request.user.is_authenticated:
            user, descricao, valor = request.user, None, None
            if 'form1' in request.POST:
                descricao = request.POST.get('descricao')
                valor = request.POST.get('valor')
                try:
                    valor = valor.replace(",", ".")
                    valor = float(valor)
                except:
                    valor = None
                if user and valor and descricao:
                    lista_geral_despesas[user] = lista_despesas.append((descricao, valor, user))
            elif 'form2' in request.POST:
                indice = request.POST.get('indice')
                try:
                    indice = int(indice) - 1
                except:
                    indice = None
                if indice:
                    lista_geral_despesas[user].pop(indice)
                else:
                    lista_geral_despesas[user].pop(0)
            lista_geral_despesas[user] = lista_despesas
            context = {}
            context['lista_despesas'] = lista_geral_despesas
            if lista_despesas:
                copy_lista = lista_despesas
                context['copia_lista_despesas'] = copy_lista
            return render(request, 'despesas.html', context)
        else:
            return redirect('conta:login')
    except:
        return redirect('conta:despesas')



lista_geral_recebimentos = {}
lista_recebimentos = []

def recebimentos(request):
    try:
        if request.user not in lista_geral_recebimentos:
            listaVaziaRecebimentos()
        if request.user.is_authenticated:
            user, descricao, valor = request.user, None, None
            if 'form1' in request.POST:
                descricao = request.POST.get('descricao')
                valor = request.POST.get('valor')

                try:
                    valor = valor.replace(",", ".")
                    valor = float(valor)
                except:
                    valor = None
                if user and valor and descricao:
                    lista_geral_recebimentos[user] = lista_recebimentos.append((descricao, valor, user))
            elif 'form2' in request.POST:
                indice = request.POST.get('indice')
                try:
                    indice = int(indice) - 1
                except:
                    indice = None
                if indice:
                    lista_geral_recebimentos[user].pop(indice)
                else:
                    lista_geral_recebimentos[user].pop(0)

            lista_geral_recebimentos[user] = lista_recebimentos
            context = {}

            context['lista_recebimentos'] = lista_geral_recebimentos
            if lista_recebimentos:
                copy_lista = lista_recebimentos
                context['copia_lista_recebimentos'] = copy_lista
            return render(request, 'recebimentos.html', context)
        else:
            return redirect('conta:login')
    except:
        return redirect('conta:despesas')

def saldoAtual(request):
    try:
        if request.user.is_authenticated:
            user = request.user
            print(user)
            lista_despesas_atual = lista_geral_despesas[user]
            lista_recebimentos_atual = lista_geral_recebimentos[user]
            context = {}
            context['lista_despesas_atual'] = lista_despesas_atual
            context['lista_recebimentos_atual'] = lista_recebimentos_atual

            return render(request, 'saldoatual.html', context)
        else:
            return redirect('conta:login')
    except:
        return redirect('conta:despesas')


def excluir_item_futuras_compras(request, item_id):
    if request.method == "DELETE":
        item = get_object_or_404(FuturasCompra, id=item_id)
        item.delete()
        return JsonResponse({"success": True})
    return JsonResponse({"success": False})

def relatorio_delete(request, relatorio_id):
    if request.method == "DELETE":
        item = get_object_or_404(Relatorio, id=relatorio_id)
        item.delete()
        return JsonResponse({"success": True})
    return JsonResponse({"success": False})

def contasfuturas_delete(request, conta_id):
    if request.method == "DELETE":
        conta = get_object_or_404(ContasAVencer, id=conta_id)
        conta.delete()
        return JsonResponse({"success": True})
    return JsonResponse({"success": False})

def criar_relatorio(request):
    try:
        from .novos_context import saldo_despesas_recebimentos

        saldo, recebimentos, soma = saldo_despesas_recebimentos(request)
        contas = lista_geral_despesas[request.user]
        recebimento = lista_geral_recebimentos[request.user]
        relatorio = Relatorio.objects.create(usuario=request.user, saldo=saldo)
        for item in contas:
            Conta.objects.create(usuario=request.user, relatoriodeconta=relatorio, descricao=item[0], valor=item[1])
        for item in recebimento:
            Recebimento.objects.create(usuario=request.user, relatorioderecebimento=relatorio, descricao=item[0], valor_pagamento=item[1])

        dicionarioItemDespesas(request)
        dicionarioItemRecebimentos(request)
        return render(request, 'relatorios.html')
    except:
        return redirect('conta:error')


def listaVaziaDespesas():
    global lista_despesas
    lista_despesas = []

def listaVaziaRecebimentos():
    global lista_recebimentos
    lista_recebimentos = []

def dicionarioItemDespesas(request):
    global lista_geral_despesas
    del lista_geral_despesas[request.user]

def dicionarioItemRecebimentos(request):
    global lista_geral_recebimentos
    del lista_geral_recebimentos[request.user]


def handler404(request, exception):
    return render(request, 'erro.html')


class ContasAVencerem(LoginRequiredMixin, FormView):
    template_name = 'contasavencer.html'
    form_class = ContasAVencerem

    def get_success_url(self):
        return reverse('conta:contasavencer')

    def get(self, request):
        form = self.form_class(user=request.user)
        return render(request, self.template_name, {'form': form})


    def post(self, request):
        form = self.form_class(request.POST, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('conta:contasavencer')
        return render(request, self.template_name, {'form': form})














