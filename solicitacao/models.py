from django.db import models
from django.contrib.auth.models import User
from accounts.models import Bairro

# Create your models here.


class AssuntoSolicitacao(models.Model):
    def __str__(self):
        return self.descricao

    class Meta:
        ordering = ['descricao']
        verbose_name_plural = "Assuntos"
        verbose_name = "Assunto"

    descricao = models.CharField(unique=True, max_length=120, verbose_name='Descrição')
    dt_inclusao = models.DateTimeField(auto_now_add=True)


class Situacao(models.Model):
    def __str__(self):
        return self.descricao

    class Meta:
        ordering = ['descricao']
        verbose_name_plural = "Situações"
        verbose_name = "Situação"

    descricao = models.CharField(unique=True, max_length=120, verbose_name='Descrição')
    dt_inclusao = models.DateTimeField(auto_now_add=True)


class Solicitacao(models.Model):
    def __str__(self):
        return self.descricao

    class Meta:
        ordering = ['-dt_inclusao']
        verbose_name_plural = "Solicitações"
        verbose_name = "Solicitação"

    assuntosolicitacao = models.ForeignKey(AssuntoSolicitacao, on_delete=models.PROTECT, verbose_name='Assunto')
    descricao = models.TextField(max_length=2000, blank=True, null=True, verbose_name='Descrição')
    foto = models.ImageField(upload_to = 'pic_folder/', default = 'pic_folder/None/no-img.jpg')
    endereco = models.CharField(max_length=120, verbose_name='Endereço', blank=True, null=True)
    numero = models.CharField(max_length=120, verbose_name='Número', blank=True, null=True)
    complemento = models.CharField(max_length=120,blank=True, null=True)
    bairro = models.ForeignKey(Bairro, on_delete=models.PROTECT, blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    situacao = models.ForeignKey(Situacao, on_delete=models.PROTECT, default=1)
    dt_inclusao = models.DateTimeField(auto_now_add=True)
