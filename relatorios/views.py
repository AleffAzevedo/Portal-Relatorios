from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponse, Http404
from .models import Relatorio
import os


def login_view(request):
    """View para login do usuário"""
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            next_url = request.GET.get('next', 'dashboard')
            return redirect(next_url)
        else:
            messages.error(request, 'Usuário ou senha inválidos.')
    
    return render(request, 'registration/login.html')


def logout_view(request):
    """View para logout do usuário"""
    logout(request)
    messages.success(request, 'Logout realizado com sucesso.')
    return redirect('login')


@login_required
def dashboard(request):
    """Dashboard principal com listagem de relatórios"""
    search_query = request.GET.get('search', '')
    tipo_filter = request.GET.get('tipo', '')
    
    relatorios = Relatorio.objects.all().order_by('-data_criacao')
    
    # Filtros de busca
    if search_query:
        relatorios = relatorios.filter(
            Q(nome__icontains=search_query) |
            Q(descricao__icontains=search_query)
        )
    
    if tipo_filter:
        relatorios = relatorios.filter(tipo=tipo_filter)
    
    # Paginação
    paginator = Paginator(relatorios, 10)  # 10 relatórios por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    # Tipos únicos para o filtro
    tipos_disponiveis = Relatorio.objects.values_list('tipo', flat=True).distinct()
    
    context = {
        'page_obj': page_obj,
        'search_query': search_query,
        'tipo_filter': tipo_filter,
        'tipos_disponiveis': tipos_disponiveis,
    }
    
    return render(request, 'relatorios/dashboard.html', context)


@login_required
def visualizar_relatorio(request, relatorio_id):
    """View para visualizar detalhes de um relatório"""
    relatorio = get_object_or_404(Relatorio, id=relatorio_id)
    return render(request, 'relatorios/visualizar.html', {'relatorio': relatorio})


@login_required
def download_relatorio(request, relatorio_id):
    """View para download de um relatório"""
    relatorio = get_object_or_404(Relatorio, id=relatorio_id)
    
    if not relatorio.arquivo:
        raise Http404("Arquivo não encontrado")
    
    file_path = relatorio.arquivo.path
    if not os.path.exists(file_path):
        raise Http404("Arquivo não encontrado no servidor")
    
    with open(file_path, 'rb') as file:
        response = HttpResponse(file.read(), content_type='application/octet-stream')
        response['Content-Disposition'] = f'attachment; filename="{relatorio.arquivo.name}"'
        return response

