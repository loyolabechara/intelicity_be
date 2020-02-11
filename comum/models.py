from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Categoria_Telefone(models.Model):
    def __str__(self):
        return self.descricao

    class Meta:
        ordering = ['descricao']
        verbose_name_plural = "Categorias de Telefones"
        verbose_name = "Categoria de Telefone"


    descricao = models.CharField(max_length=120)
    user = models.ManyToManyField(User)
    dt_inclusao = models.DateTimeField(auto_now_add=True)

class Telefone(models.Model):
    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['nome']

    categoria_telefone = models.ForeignKey(Categoria_Telefone, on_delete=models.PROTECT)
    nome = models.CharField(max_length=120)
    numero = models.CharField(max_length=11)
    mensageiro = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    dt_inclusao = models.DateTimeField(auto_now_add=True)
