from django.test import TestCase
from .models import AtividadeModel
from datetime import datetime


class IndexTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/')

    def test_200(self):
        self.assertEqual(200, self.resp.status_code)

    def test_Texto(self):
        self.assertContains(self.resp, 'hoje')

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'index.html')


class AtividadeModelTest(TestCase):
    def setUp(self):
        self.cadastro = AtividadeModel(
            titulo='Teste Titulo',
            data='2023-06-09',
            local='Teste local',
            tarefa='Teste tarefa'
        )
        self.cadastro.save()

    def test_criado(self):
        self.assertTrue(AtividadeModel.objects.exists())

    def test_criado_somente_um(self):
        self.assertTrue(len(AtividadeModel.objects.all()) == 1)

    def test_modificado_em(self):
        self.assertIsInstance(self.cadastro.modificado_em, datetime)
