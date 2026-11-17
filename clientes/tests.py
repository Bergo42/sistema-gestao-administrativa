from django.test import TestCase
from django.urls import reverse
from .models import Cliente


class ClienteModelTest(TestCase):

    def test_criar_cliente(self):
        cliente = Cliente.objects.create(
            nome='Maria Silva',
            telefone='61999999999',
            email='maria@email.com'
        )

        self.assertEqual(cliente.nome, 'Maria Silva')
        self.assertEqual(str(cliente), 'Maria Silva')


class ClienteViewTest(TestCase):

    def test_listar_clientes(self):
        Cliente.objects.create(
            nome='Joao Santos',
            telefone='61988888888'
        )

        response = self.client.get(reverse('listar_clientes'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Joao Santos')

    def test_cadastrar_cliente(self):
        response = self.client.post(
            reverse('cadastrar_cliente'),
            {
                'nome': 'Carlos Souza',
                'telefone': '61977777777',
                'email': 'carlos@email.com'
            }
        )

        self.assertEqual(response.status_code, 302)
        self.assertTrue(
            Cliente.objects.filter(nome='Carlos Souza').exists()
        )