from django.contrib import admin
from .models import Catalogo


@admin.register(Catalogo)
class CatalogoAdmin(admin.ModelAdmin):
    list_display = ('nombre_catalogo', 'especie', 'genero', 'dia_creacion')


