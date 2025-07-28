from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('relatorio/<int:relatorio_id>/', views.visualizar_relatorio, name='visualizar_relatorio'),
    path('relatorio/<int:relatorio_id>/download/', views.download_relatorio, name='download_relatorio'),
]

