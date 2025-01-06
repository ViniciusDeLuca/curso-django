from django.contrib import admin
from .models import Categoria, Receita

class CategoriaAdmin(admin.ModelAdmin):
    ...

@admin.register(Receita)
class ReceitaAdmin(admin.ModelAdmin):
    ...

admin.site.register(Categoria, CategoriaAdmin)
