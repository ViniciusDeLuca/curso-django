from django.test import TestCase
from django.urls import reverse

class ReceitaURLsTest(TestCase):
    def test_inicio_url_esta_correto(self):
        url = reverse('inicio')
        print(url)
        self.assertEqual(url, '/')
    
    def test_categoria_receita_url_esta_correto(self):
        url = reverse('receitas_por_categorias', kwargs={'categoria_id': 1})
        print(url)
        self.assertEqual(url, '/receita/categoria/1/')