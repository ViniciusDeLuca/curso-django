from django.db import models

class Receita(models.Model):
    titulo = models.CharField(max_length=120)
    descricao = models.CharField(max_length=165)
    tempo_preparo = models.IntegerField()
    unidade_preparo = models.CharField(max_length=50)
    unidades_porcao = models.IntegerField()
    etapas_preparo = models.TextField()
    etapas_preparo_is_html = models.BooleanField(default=False)
    publicado = models.BooleanField(default=True)
    capa = models.ImageField(upload_to='receitas/capas/%Y/%m/%d/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)