from django.test import TestCase
from aluraflix.models import Programa

class FixtureDataTestCase(TestCase):

    fixtures = ['programas_iniciais']

    def test_verifica_carregamento_da_fixture(self):
        programa_ruim = Programa.objects.get(pk=1)
        todos_os_programas = Programa.objects.all()
        self.assertEqual(programa_ruim.titulo, 'Coisas bizarras')
        self.assertEqual(len(todos_os_programas), 9)