from django.test import TestCase
from django.urls import reverse
from datetime import date, timedelta
from clientes.models import Cliente
from .models import Solicitacao


class SolicitacaoModelTest(TestCase):

    def setUp(self):
        self.cliente = Cliente.objects.create(
            nome='Maria Silva',
            telefone='61999999999'
        )

    def test_criar_solicitacao(self):
        solicitacao = Solicitacao.objects.create(
            cliente=self.cliente,
            descricao='Organizacao de documentos',
            prazo=date.today() + timedelta(days=10)
        )

        self.assertEqual(solicitacao.cliente, self.cliente)
        self.assertEqual(solicitacao.status, 'Pendente')
        self.assertIn('Maria Silva', str(solicitacao))


class SolicitacaoViewTest(TestCase):

    def setUp(self):
        self.cliente = Cliente.objects.create(
            nome='Joao Santos',
            telefone='61988888888'
        )

    def test_listar_solicitacoes(self):
        Solicitacao.objects.create(
            cliente=self.cliente,
            descricao='Servico administrativo',
            prazo=date.today() + timedelta(days=5)
        )

        response = self.client.get(reverse('listar_solicitacoes'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Joao Santos')
        self.assertContains(response, 'Servico administrativo')

    def test_cadastrar_solicitacao(self):
        response = self.client.post(
            reverse('cadastrar_solicitacao'),
            {
                'cliente': self.cliente.id,
                'descricao': 'Cadastro de documentos',
                'prazo': (date.today() + timedelta(days=7)).isoformat(),
                'status': 'Pendente'
            }
        )

        self.assertEqual(response.status_code, 302)
        self.assertTrue(
            Solicitacao.objects.filter(
                descricao='Cadastro de documentos'
            ).exists()
        )