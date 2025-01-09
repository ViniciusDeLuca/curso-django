from .test_receita_base import ReceitaBaseTest
from django.core.exceptions import ValidationError

class CategoriaReceitaModelsTest(ReceitaBaseTest):
    def setUp(self):
        self.categoria = self.cria_categoria()
        return super().setUp()
    
    def test_nome_categoria_receita_gera_erro_se_excender_tamanho(self):
        self.categoria.nome = 'A' * 121
        with self.assertRaises(ValidationError):
            self.categoria.full_clean()
        
    def test_representacao_do_model_categoria_em_string(self):
        self.categoria.nome = 'Almoço'
        self.categoria.full_clean()
        self.categoria.save()
        
        self.assertEqual(str(self.categoria), 'Almoço')