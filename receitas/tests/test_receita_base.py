from django.test import TestCase
from receitas.models import Receita, Categoria, User

class ReceitaBaseTest(TestCase):
    def setUp(self):
        categoria = Categoria.objects.create(nome="Sobremesas")
        
        autor = User.objects.create_user(username="autor_teste", password="senha123")
        
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
        return super().setUp()
