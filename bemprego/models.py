from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Escolaridade(models.Model):
    def __str__(self):
        return self.descricao

    class Meta:
        ordering = ['id']

    descricao = models.CharField(max_length=120)
    dt_inclusao = models.DateTimeField(auto_now_add=True)


class Cargo(models.Model):
    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['nome']

    nome = models.CharField(max_length=120)
    dt_inclusao = models.DateTimeField(auto_now_add=True)


class Vaga(models.Model):
    SEXO = (
        ('A', 'Ambos'),
        ('F', 'Feminino'),
        ('M', 'Masculino'),
    )

    def __int__(self):
        return self.cargo

    class Meta:
        ordering = ['cargo']

    cargo = models.ForeignKey(Cargo, on_delete=models.PROTECT)
    sexo = models.CharField(max_length=1, choices=SEXO)
    experiencia = models.BooleanField(default=False)
    escolaridade = models.ForeignKey(Escolaridade, on_delete=models.PROTECT)
    dt_fim = models.DateTimeField('Dt. Retirada')
    dt_inclusao = models.DateTimeField(auto_now_add=True)
