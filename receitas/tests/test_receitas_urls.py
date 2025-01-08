from django.test import TestCase
from django.urls import reverse

class ReceitaURLsTest(TestCase):
    def test_inicio_url_esta_correto(self):
        url = reverse('inicio')
        self.assertEqual(url, '/')
    
    def test_categoria_receita_url_esta_correto(self):
        url = reverse('receitas_por_categorias', kwargs={'categoria_id': 1})
        self.assertEqual(url, '/receita/categoria/1/')
    
    def test_detalhe_receita_url_esta_correto(self):
        url = reverse('receita_detalhe', kwargs={'id': 1})
        self.assertEqual(url, '/receita/1/')