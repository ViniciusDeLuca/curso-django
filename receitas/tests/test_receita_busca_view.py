from django.urls import reverse, resolve
from receitas import views
from receitas.tests.test_receita_base import ReceitaBaseTest

class ReceitaViewsTest(ReceitaBaseTest):        
    def test_busca_de_receita_utiliza_a_funcao_correta(self):
        resolved = resolve(reverse('busca'))
        self.assertIs(resolved.func, views.busca)
        
    def test_carrega_o_template_correto_para_busca_de_receita(self):
        response = self.client.get(reverse('busca') + '?q=asd')
        self.assertTemplateUsed(
            response,
            'paginas/busca.html')
    
    def test_url_busca_retorna_404_com_termo_vazio(self):
        response = self.client.get(reverse('busca'))
        self.assertEqual(response.status_code, 404)
        
    def test_valor_de_busca_esta_escapado(self):
        url = reverse('busca') + '?q=teste'
        response = self.client.get(url)
        self.assertIn(
            'Busca por "teste"',
            response.content.decode('utf-8')
        )