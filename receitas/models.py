from django.db import models
from django.contrib.auth.models import User

class ReceitaQuerySet(models.QuerySet):
    def publicado(self):
        return self.filter(esta_publicado=True)
    
class ReceitaManager(models.Manager):
    def get_queryset(self):
        return ReceitaQuerySet(self.model, using=self._db).filter(esta_publicado=True)

class Categoria(models.Model):
    nome = models.CharField(max_length=120)

    def __str__(self):
        return self.nome

class Receita(models.Model):
    titulo = models.CharField(max_length=120)
    descricao = models.CharField(max_length=165)
    tempo_preparo = models.IntegerField()
    unidade_tempo = models.CharField(max_length=30, default='Minutos')
    unidade_preparo = models.CharField(max_length=50)
    unidades_porcao = models.IntegerField()
    etapas_preparo = models.TextField()
    etapas_preparo_is_html = models.BooleanField(default=False)
    esta_publicado = models.BooleanField(default=True)
    capa = models.ImageField(upload_to='receitas/capas/%Y/%m/%d/', blank=True, default='')
    slug = models.SlugField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True, default=None)
    autor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, default=None)

    def __str__(self):
        return self.titulo
    
    objects = ReceitaManager()