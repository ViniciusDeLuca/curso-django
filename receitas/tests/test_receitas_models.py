from django.test import TestCase
from receitas.models import Receita, Categoria
from django.contrib.auth.models import User

class ReceitaModelsTest(TestCase):
    
    def test_receita_model(self):
        # Criação de instância de Categoria
        categoria = Categoria.objects.create(nome="Sobremesas")
        
        # Criação de instância de User
        autor = User.objects.create_user(username="autor_teste", password="senha123")
        
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