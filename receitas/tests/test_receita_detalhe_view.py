from django.urls import reverse, resolve
from receitas import views
from receitas.tests.test_receita_base import ReceitaBaseTest

class ReceitaDetalheViewsTest(ReceitaBaseTest):        
    def test_detalhe_receita_mostra_a_receita_correta(self):
        titulo = 'Titulo para essa receita'
        self.cria_receita(titulo=titulo)
        
        response = self.client.get(
            reverse('receita_detalhe',
                    kwargs={'id': 1}
                    )
        )
        conteudo = response.content.decode('utf-8')
        
        self.assertIn(titulo, conteudo)
        
    def test_detalhe_receita_view_esta_correto(self):
        view = resolve(reverse('receita_detalhe', kwargs={'id': 29}))
        self.assertIs(view.func, views.receitaDetalhe)
        
    def test_detalhe_receita_view_retorna_status_404_nao_encontrado(self):
        response = self.client.get(reverse('receita_detalhe', kwargs={'id': 2}))
        self.assertEqual(response.status_code, 404)