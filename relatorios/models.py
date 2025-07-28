from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Relatorio(models.Model):
    """Modelo para armazenar informações dos relatórios"""
    
    TIPOS_RELATORIO = [
        ('financeiro', 'Financeiro'),
        ('vendas', 'Vendas'),
        ('marketing', 'Marketing'),
        ('operacional', 'Operacional'),
        ('rh', 'Recursos Humanos'),
        ('outros', 'Outros'),
    ]
    
    nome = models.CharField(max_length=200, verbose_name='Nome do Relatório')
    descricao = models.TextField(blank=True, verbose_name='Descrição')
    tipo = models.CharField(
        max_length=20, 
        choices=TIPOS_RELATORIO, 
        default='outros',
        verbose_name='Tipo'
    )
    arquivo = models.FileField(
        upload_to='relatorios/%Y/%m/',
        verbose_name='Arquivo',
        blank=True,
        null=True
    )
    data_criacao = models.DateTimeField(
        default=timezone.now,
        verbose_name='Data de Criação'
    )
    criado_por = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Criado por'
    )
    ativo = models.BooleanField(default=True, verbose_name='Ativo')
    
    class Meta:
        verbose_name = 'Relatório'
        verbose_name_plural = 'Relatórios'
        ordering = ['-data_criacao']
    
    def __str__(self):
        return self.nome
    
    def get_tipo_display_custom(self):
        """Retorna o nome do tipo formatado"""
        return dict(self.TIPOS_RELATORIO).get(self.tipo, self.tipo)
    
    def get_tamanho_arquivo(self):
        """Retorna o tamanho do arquivo formatado"""
        if self.arquivo:
            size = self.arquivo.size
            if size < 1024:
                return f"{size} bytes"
            elif size < 1024 * 1024:
                return f"{size / 1024:.1f} KB"
            else:
                return f"{size / (1024 * 1024):.1f} MB"
        return "N/A"

