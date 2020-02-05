from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Assunto(models.Model):
    def __str__(self):
        return self.descricao

    class Meta:
        ordering = ['descricao']

    descricao = models.CharField(max_length=120)
    user = models.ManyToManyField(User)
    dt_inclusao = models.DateTimeField(auto_now_add=True)

# TODO: Colocar repetição na agenda

class Agenda(models.Model):
    def __str__(self):
        return self.titulo

    class Meta:
        ordering = ['dt_evento', 'titulo']

    titulo = models.CharField(max_length=120)
    descricao = models.TextField(max_length=2000, blank=True, null=True)
    assunto = models.ForeignKey(Assunto, on_delete=models.PROTECT)
    dt_evento = models.DateTimeField('Data:')
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    dt_inclusao = models.DateTimeField(auto_now_add=True)
