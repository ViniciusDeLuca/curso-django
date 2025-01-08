from django.test import TestCase
from receitas.models import Receita, Categoria, User

class ReceitaBaseTest(TestCase):
    def setUp(self):
        return super().setUp()
        
    def cria_categoria(self, nome='Sobremesas'):
        return Categoria.objects.create(nome=nome)
    
    def cria_autor(
        self,
        first_name='usuario',
        last_name='last name',
        username='username',
        password='1234@Abc',
        email='usuario@email.com'
    ):
        return User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            password=password,
            email=email
        )
    
    def cria_receita(
        self,
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
        dados_categoria=None,
        dados_autor=None
    ):
        if dados_categoria is None:
            dados_categoria = {}
            
        if dados_autor is None:
            dados_autor = {}
        return Receita.objects.create(
            categoria=self.cria_categoria(**dados_categoria),
            autor=self.cria_autor(**dados_autor),
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
        )