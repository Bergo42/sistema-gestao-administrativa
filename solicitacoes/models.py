from django.db import models
from clientes.models import Cliente


class Solicitacao(models.Model):

    STATUS_CHOICES = [
        ('Pendente', 'Pendente'),
        ('Em andamento', 'Em andamento'),
        ('Concluída', 'Concluída'),
    ]

    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE,
        related_name='solicitacoes'
    )

    descricao = models.TextField()
    data_registro = models.DateTimeField(auto_now_add=True)
    prazo = models.DateField()
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Pendente'
    )

    def __str__(self):
        return f'{self.cliente.nome} - {self.descricao[:50]}'

    class Meta:
        ordering = ['prazo']
        verbose_name = 'Solicitação'
        verbose_name_plural = 'Solicitações'