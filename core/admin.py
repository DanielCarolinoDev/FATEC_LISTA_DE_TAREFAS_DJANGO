from django.contrib import admin
from .models import AtividadeModel

class AtividadeModelAdmin(admin.ModelAdmin):
    list_display = ('titulo','data','local','tarefa')
    date_hierarchy = 'data'
    search_fields = ('titulo','data')

admin.site.register(AtividadeModel, AtividadeModelAdmin)
