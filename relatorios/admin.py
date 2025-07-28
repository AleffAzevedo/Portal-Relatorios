from django.contrib import admin
from .models import Relatorio


@admin.register(Relatorio)
class RelatorioAdmin(admin.ModelAdmin):
    """Configuração do admin para o modelo Relatorio"""
    
    list_display = ['nome', 'tipo', 'criado_por', 'data_criacao', 'ativo']
    list_filter = ['tipo', 'ativo', 'data_criacao', 'criado_por']
    search_fields = ['nome', 'descricao']
    list_editable = ['ativo']
    list_per_page = 20
    
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('nome', 'descricao', 'tipo')
        }),
        ('Arquivo', {
            'fields': ('arquivo',)
        }),
        ('Configurações', {
            'fields': ('ativo',)
        }),
        ('Metadados', {
            'fields': ('criado_por', 'data_criacao'),
            'classes': ('collapse',)
        }),
    )
    
    readonly_fields = ['data_criacao']
    
    def save_model(self, request, obj, form, change):
        """Automaticamente define o usuário criador se não estiver definido"""
        if not change:  # Se é um novo objeto
            obj.criado_por = request.user
        super().save_model(request, obj, form, change)

