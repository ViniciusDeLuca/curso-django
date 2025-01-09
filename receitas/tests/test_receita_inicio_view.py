from django.urls import reverse, resolve
from receitas import views
from receitas.tests.test_receita_base import ReceitaBaseTest

class ReceitaInicioViewsTest(ReceitaBaseTest):
    
    def test_inicio_view_esta_correto(self):
        view = resolve(reverse('inicio'))
        self.assertIs(view.func, views.inicio)
        
    def test_inicio_view_retorna_status_200_ok(self):
        response = self.client.get(reverse('inicio'))
        self.assertEqual(response.status_code, 200)
        
    def test_inicio_view_carrega_template_correto(self):
        response = self.client.get(reverse('inicio'))
        self.assertTemplateUsed(response, 'paginas/inicio.html')
        
    def test_inicio_lista_nenhuma_receita_encontrada_caso_nao_tenha_receitas(self):
        response = self.client.get(reverse('inicio'))
        self.assertIn(
            'Não foram encontradas receitas',
            response.content.decode('utf-8')
        )
        
    def test_inicio_template_carrega_receitas(self):
        self.cria_receita()
        response = self.client.get(reverse('inicio'))
        
        response_content = response.content.decode('utf-8')
        self.assertIn(
            'Bolo de Cenoura',
            response_content
        )
    
    def test_inicio_template_não_lista_receitas_nao_publicadas(self):
        self.cria_receita(esta_publicado=False)
        
        response = self.client.get(reverse('inicio'))
        
        conteudo = response.content.decode('utf-8')

        self.assertIn(
            'Não foram encontradas receitas',
            conteudo
        )