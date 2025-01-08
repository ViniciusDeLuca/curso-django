from django.urls import reverse, resolve
from receitas import views
from receitas.tests.test_receita_base import ReceitaBaseTest

class ReceitaViewsTest(ReceitaBaseTest):
    
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
        
    def test_categoria_receita_view_esta_correto(self):
        view = resolve(reverse('receitas_por_categorias', kwargs={'categoria_id': 1}))
        self.assertIs(view.func, views.receitaCategoria)
        
    def test_categoria_receita_mostra_a_receita_correta(self):
        titulo = 'Titulo para essa receita'
        self.cria_receita(titulo=titulo)
        
        response = self.client.get(
            reverse('receitas_por_categorias',
                    kwargs={'categoria_id': 1}
                    )
        )
        conteudo = response.content.decode('utf-8')
        
        self.assertIn(titulo, conteudo)
        
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
        
    def test_inicio_template_não_lista_receitas_nao_publicadas(self):
        self.cria_receita(esta_publicado=False)
        
        response = self.client.get(reverse('inicio'))
        
        conteudo = response.content.decode('utf-8')

        self.assertIn(
            'Não foram encontradas receitas',
            conteudo
        )
        
    # rodar somente se tiver algo inserido no banco temporario
    # def test_categoria_view_retorna_status_200_ok(self):
    #     response = self.client.get(reverse('receitas_por_categorias', kwargs={'categoria_id': 2}))
    #     self.assertEqual(response.status_code, 200)
        
    # def test_categoria_view_carrega_template_correto(self):
    #     response = self.client.get(reverse('receitas_por_categorias', kwargs={'categoria_id': 2}))
    #     self.assertTemplateUsed(response, 'paginas/receita-categoria.html')
        
    # def test_categoria_lista_nenhuma_receita_encontrada_caso_nao_tenha_receitas(self):
    #     response = self.client.get(reverse('receitas_por_categorias', kwargs={'categoria_id': 2}))
    #     self.assertIn(
    #         'ver mais...',
    #         response.content.decode('utf-8')
    #     )
    
    def test_categoria_view_retorna_status_404_nao_encontrado(self):
        response = self.client.get(reverse('receitas_por_categorias', kwargs={'categoria_id': 1000}))
        self.assertEqual(response.status_code, 404)
        
    def test_categoria_template_não_lista_receitas_nao_publicadas(self):
        receita = self.cria_receita(esta_publicado=False)
        
        response = self.client.get(reverse('receitas_por_categorias',
                                        kwargs={'categoria_id': receita.categoria.id}
                                        ))
        
        self.assertEqual(
            response.status_code, 404
            )    
        
    def test_detalhe_receita_view_esta_correto(self):
        view = resolve(reverse('receita_detalhe', kwargs={'id': 29}))
        self.assertIs(view.func, views.receitaDetalhe)
        
    def test_detalhe_receita_view_retorna_status_404_nao_encontrado(self):
        response = self.client.get(reverse('receita_detalhe', kwargs={'id': 2}))
        self.assertEqual(response.status_code, 404)
        