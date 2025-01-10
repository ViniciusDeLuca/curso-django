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
    
    def test_busca_receita_consegue_pesquisar_por_titulo(self):
        titulo1 = 'Receita Um'
        titulo2 = 'Receita Dois'
        
        receita1 = self.cria_receita(
            slug='um',
            titulo=titulo1,
            dados_autor={'username': 'um'}
        )
        receita2 = self.cria_receita(
            slug='dois',
            titulo=titulo2,
            dados_autor={'username': 'dois'}
        )
        
        url = reverse('busca')
        response1 = self.client.get(f'{url}?q={titulo1}')
        response2 = self.client.get(f'{url}?q={titulo2}')
        response_ambas = self.client.get(f'{url}?q=Receita')
        
        self.assertIn(titulo1,[receita.titulo for receita in response1.context['receitas']])
        self.assertNotIn(titulo2,[receita.titulo for receita in response1.context['receitas']])
        
        self.assertIn(titulo2,[receita.titulo for receita in response2.context['receitas']])
        self.assertNotIn(titulo1,[receita.titulo for receita in response2.context['receitas']])
        
        self.assertIn(titulo1,[receita.titulo for receita in response_ambas.context['receitas']])
        self.assertIn(titulo2,[receita.titulo for receita in response_ambas.context['receitas']])