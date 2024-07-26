from django.contrib import admin
from .models import Criancas

class CriancasAdmin(admin.ModelAdmin):
    list_display=("id", "nome", "nomeMae", "vacina", "bairro")

admin.site.register(Criancas, CriancasAdmin)

