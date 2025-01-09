from django.contrib.auth.models import User
from .test_receita_base import ReceitaBaseTest
from django.core.exceptions import ValidationError
from parameterized import parameterized
from receitas.models import Receita
class ReceitaModelsTest(ReceitaBaseTest):
    def setUp(self):
        self.receita = self.cria_receita()
        return super().setUp()
    
    def test_titulo_receita_gera_erro_se_excender_tamanho(self):
        self.receita.titulo = 'A' * 121
        with self.assertRaises(ValidationError):
            self.receita.full_clean()
    
    def test_receita_model(self):
        # Criação de instância de Categoria
        categoria = self.cria_categoria
        
        # Criação de instância de User
        autor = self.cria_autor
        
        # Criação de instância de Receita
        receita = Receita.objects.create(
            titulo="Bolo de Cenoura",
            descricao="Delicioso bolo com cobertura de chocolate",
            tempo_preparo=60,
            unidade_tempo="Minutos",
            unidade_preparo="Porções",
            unidades_porcao=10,
            etapas_preparo="1. Misture os ingredientes.\n2. Leve ao forno por 40 minutos.",
            etapas_preparo_is_html=False,
            esta_publicado=True,
            capa="",
            slug="bolo-de-cenoura",
            categoria=categoria,
            autor=autor,
        )

        # Verifica se os campos foram criados corretamente
        self.assertEqual(receita.titulo, "Bolo de Cenoura")
        self.assertEqual(receita.descricao, "Delicioso bolo com cobertura de chocolate")
        self.assertEqual(receita.tempo_preparo, 60)
        self.assertEqual(receita.unidade_tempo, "Minutos")
        self.assertEqual(receita.unidade_preparo, "Porções")
        self.assertEqual(receita.unidades_porcao, 10)
        self.assertEqual(receita.etapas_preparo, "1. Misture os ingredientes.\n2. Leve ao forno por 40 minutos.")
        self.assertFalse(receita.etapas_preparo_is_html)
        self.assertTrue(receita.esta_publicado)
        self.assertEqual(receita.slug, "bolo-de-cenoura")
        self.assertEqual(receita.categoria, categoria)
        self.assertEqual(receita.autor, autor)

        # Verifica o método __str__
        self.assertEqual(str(receita), "Bolo de Cenoura")
        
    @parameterized.expand([
        ('titulo', 120),
        ('descricao', 165),
        ('unidade_tempo', 30),
        ('unidade_preparo', 50)
    ])
    def test_tamanho_maximo_dos_campos_de_receita(self, campo, tamanho_maximo):
        setattr(self.receita, campo, 'A' * (tamanho_maximo + 1))
        with self.assertRaises(ValidationError):
            self.receita.full_clean()
        
    def test_representacao_do_model_receita_em_string(self):
        self.receita.titulo = 'Tapioca de queijo'
        self.receita.full_clean()
        self.receita.save()
        
        self.assertEqual(str(self.receita), 'Tapioca de queijo')