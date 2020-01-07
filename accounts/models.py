from django.db import models
from django.contrib.auth.models import User

from .functions import validate_CPF

# Create your models here.

class Cidade(models.Model):
    def __str__(self):
        return self.nome

    class Meta:
        ordering = ('nome',)

    nome = models.CharField(max_length=30)
    dt_inclusao = models.DateTimeField(auto_now_add=True)

class Bairro(models.Model):
    def __str__(self):
        return '%s' % (self.nome)

    class Meta:
        ordering = ('cidade', 'nome',)

    cidade = models.ForeignKey(Cidade, on_delete=models.PROTECT)
    nome = models.CharField(max_length=30)
    dt_inclusao = models.DateTimeField(auto_now_add=True)


class Usuario(models.Model):

    SEXO = (
        ('F', 'Feminino'),
        ('M', 'Masculino'),
    )

    class Meta:
#        verbose_name_plural = "Instrutores"
        verbose_name = "Usuário"
        ordering = ('user',)

    def __str__(self):
        return '%s' % (self.user)

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cpf = models.CharField(unique=True, max_length=11, validators=[validate_CPF])
    celular = models.CharField(max_length=11)
    email = models.CharField(unique = True, blank=True, null=True, max_length=120)
    sexo = models.CharField(max_length=1, choices=SEXO)
    endereco = models.CharField(max_length=120, blank=True, null=True)
    numero = models.CharField(max_length=60, blank=True, null=True)
    complemento = models.CharField(max_length=120, blank=True, null=True)
    bairro = models.ForeignKey(Bairro, on_delete=models.PROTECT)
    cep = models.CharField(max_length=8, blank=True, null=True)
    dt_nascimento = models.DateField('Data Nascimento')
    dt_inclusao = models.DateTimeField(auto_now_add=True)
    ativo = models.BooleanField(default=True)
