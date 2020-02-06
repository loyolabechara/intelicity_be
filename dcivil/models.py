from django.db import models
from django.contrib.auth.models import User
from accounts.models import Bairro

# Create your models here.


class Dirigente(models.Model):
    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['nome']

    nome = models.CharField(max_length=120)
    celular = models.CharField(max_length=11, blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    dt_inclusao = models.DateTimeField(auto_now_add=True)

class Responsavel(models.Model):
    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['nome']
        verbose_name_plural = "Responsáveis"
        verbose_name = "Responsável"

    nome = models.CharField(max_length=120)
    celular = models.CharField(max_length=11, blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    dt_inclusao = models.DateTimeField(auto_now_add=True)

class Ponto_Apoio(models.Model):
    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['nome']
        verbose_name_plural = "Pontos de Apoio"
        verbose_name = "Ponto de Apoio"

    nome = models.CharField(max_length=120)
    diretor = models.CharField(max_length=60, blank=True, null=True)
    dirigente = models.ManyToManyField(Dirigente, blank=True)
    responsavel = models.ManyToManyField(Responsavel, blank=True)
    celular = models.CharField(max_length=11, blank=True, null=True)
    telefone = models.CharField(max_length=10, blank=True, null=True)
    email = models.EmailField(blank=True, null=True, max_length=120)
    endereco = models.CharField(max_length=120)
    numero = models.CharField(max_length=120)
    complemento = models.CharField(max_length=120,blank=True, null=True)
    bairro = models.ForeignKey(Bairro, on_delete=models.PROTECT)
    capacidade = models.PositiveSmallIntegerField(default=1)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    dt_inclusao = models.DateTimeField(auto_now_add=True)

class Alerta(models.Model):
    def __str__(self):
        return self.estagio

    class Meta:
        ordering = ['id']

    estagio = models.CharField(max_length=120)
    descricao = models.CharField(max_length=2000)
    dt_inclusao = models.DateTimeField(auto_now_add=True)

class Historico_Alerta(models.Model):
    def __int__(self):
        return self.alerta

    class Meta:
        ordering = ['-dt_inclusao']
        verbose_name_plural = "Históricos de Alerta"
        verbose_name = "Histórico de Alerta"

    alerta = models.ForeignKey(Alerta, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    dt_inclusao = models.DateTimeField(auto_now_add=True)
