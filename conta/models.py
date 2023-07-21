from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser



def mes():
    from datetime import date
    data_atual = date.today()
    mes_atual = f'{data_atual.day}/{data_atual.month}/{data_atual.year}'
    return mes_atual

class Conta(models.Model):
    usuario = models.ForeignKey("Usuario", related_name="contas_usuarios", on_delete=models.CASCADE)
    relatoriodeconta = models.ForeignKey("Relatorio", related_name="contas", on_delete=models.CASCADE)
    descricao = models.CharField(max_length=150)
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.relatoriodeconta.descricao +" - " +self.descricao


class Recebimento(models.Model):
    usuario = models.ForeignKey("Usuario", related_name="recebimentos_usuario", on_delete=models.CASCADE)
    relatorioderecebimento = models.ForeignKey("Relatorio", related_name="recebimentos", on_delete=models.CASCADE)
    descricao = models.CharField(max_length=150)
    valor_pagamento = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.relatorioderecebimento.descricao +" - "+self.descricao


class FuturasCompra(models.Model):
    usuario = models.ForeignKey("Usuario", related_name="futurascompras", on_delete=models.CASCADE)
    descricao = models.CharField(max_length=150)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    url = models.URLField(blank=True, null=True)


    def __str__(self):
        return self.descricao


class Relatorio(models.Model):
    usuario = models.ForeignKey("Usuario", related_name="relatorios", on_delete=models.CASCADE)
    saldo = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    descricao = models.CharField(max_length=150, default=mes)
    data_lancamento = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.descricao



class Usuario(AbstractUser):
    data_criacao = models.DateTimeField(default=timezone.now)

