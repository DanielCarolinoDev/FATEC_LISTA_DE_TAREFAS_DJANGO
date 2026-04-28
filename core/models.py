from django.db import models


class AtividadeModel(models.Model):
    id = models.IntegerField().primary_key
    titulo = models.CharField('titulo', max_length=50)
    data = models.DateField('data')
    local = models.CharField('local', max_length=50)
    tarefa = models.CharField('tarefa', max_length=200)

    modificado_em = models.DateTimeField(
        verbose_name='modificado em',
        auto_now_add=False, auto_now=True)

    def __str__(self):
        return "{} ({},{},{})".format(self.titulo, self.data, self.local, self.tarefa)
