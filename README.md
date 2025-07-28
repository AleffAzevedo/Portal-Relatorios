# Portal de Relatórios

Um portal simples e elegante desenvolvido em Django para alocar e visualizar relatórios da empresa. O sistema oferece uma interface clean e responsiva para organizar relatórios por nome, data, tipo e outras características, com opções de visualização e download.

## 🚀 Funcionalidades

- **Autenticação**: Sistema de login/logout usando o auth padrão do Django
- **Gestão de Relatórios**: Upload, visualização e download de relatórios
- **Organização**: Filtros por tipo, busca por nome/descrição e paginação
- **Interface Responsiva**: Design clean com Bootstrap 5
- **Painel Administrativo**: Gerenciamento completo via Django Admin
- **Deploy Ready**: Configurado para deploy no Render.com

## 🛠️ Tecnologias Utilizadas

- **Backend**: Django 5.2.4
- **Frontend**: Bootstrap 5.3.0 + Bootstrap Icons
- **Banco de Dados**: SQLite (desenvolvimento) / PostgreSQL (produção)
- **Deploy**: Render.com
- **Servidor**: Gunicorn
- **Arquivos Estáticos**: WhiteNoise

## 📋 Pré-requisitos

- Python 3.8+
- pip (gerenciador de pacotes Python)
- Git




## 🔧 Instalação e Execução Local

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/portal-relatorios.git
cd portal-relatorios
```

### 2. Crie um ambiente virtual

```bash
python -m venv venv

# No Windows
venv\Scripts\activate

# No Linux/Mac
source venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure as variáveis de ambiente

Copie o arquivo `.env.example` para `.env` e ajuste as configurações:

```bash
cp .env.example .env
```

Edite o arquivo `.env` com suas configurações:

```env
SECRET_KEY=sua-chave-secreta-aqui
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

### 5. Execute as migrações

```bash
python manage.py migrate
```

### 6. Crie um superusuário

```bash
python manage.py createsuperuser
```

### 7. Colete os arquivos estáticos

```bash
python manage.py collectstatic
```

### 8. Execute o servidor de desenvolvimento

```bash
python manage.py runserver
```

O sistema estará disponível em: `http://localhost:8000`

### 9. Acesse o painel administrativo

Acesse `http://localhost:8000/admin` com as credenciais do superusuário criado para gerenciar usuários e relatórios.


## 🌐 Deploy no Render.com

### 1. Preparação do Repositório

Certifique-se de que todos os arquivos estão commitados no seu repositório GitHub:

```bash
git add .
git commit -m "Projeto portal de relatórios completo"
git push origin main
```

### 2. Configuração no Render.com

1. **Acesse o Render.com** e faça login
2. **Clique em "New +"** e selecione "Web Service"
3. **Conecte seu repositório GitHub** com o projeto
4. **Configure o serviço**:
   - **Name**: `portal-relatorios` (ou nome de sua escolha)
   - **Environment**: `Python 3`
   - **Build Command**: `./build.sh`
   - **Start Command**: `gunicorn portal_relatorios.wsgi:application --bind 0.0.0.0:$PORT`

### 3. Configuração das Variáveis de Ambiente

No painel do Render, vá para a aba "Environment" e adicione:

```env
SECRET_KEY=sua-chave-secreta-super-segura-aqui
DEBUG=False
ALLOWED_HOSTS=seu-app.onrender.com
```

**⚠️ Importante**: 
- Gere uma SECRET_KEY segura (pode usar: `python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"`)
- Substitua `seu-app.onrender.com` pelo domínio real do seu app no Render

### 4. Deploy

1. **Clique em "Create Web Service"**
2. **Aguarde o build** (pode levar alguns minutos)
3. **Acesse a URL** fornecida pelo Render

### 5. Configuração Pós-Deploy

Após o primeiro deploy bem-sucedido:

1. **Acesse o shell do Render** (via dashboard)
2. **Crie um superusuário**:
   ```bash
   python manage.py createsuperuser
   ```

### 6. Banco de Dados (Opcional)

Para produção, recomenda-se usar PostgreSQL:

1. **No Render**, crie um novo "PostgreSQL Database"
2. **Adicione a variável** `DATABASE_URL` nas configurações do web service
3. **Instale psycopg2** adicionando ao `requirements.txt`:
   ```
   psycopg2-binary==2.9.7
   ```

### 7. Domínio Personalizado (Opcional)

No painel do Render, você pode configurar um domínio personalizado na aba "Settings".


## 📁 Estrutura do Projeto

```
portal_relatorios/
├── portal_relatorios/          # Configurações do projeto
│   ├── settings.py            # Configurações principais
│   ├── urls.py               # URLs principais
│   └── wsgi.py               # WSGI para deploy
├── relatorios/               # App principal
│   ├── models.py             # Modelo Relatorio
│   ├── views.py              # Views do sistema
│   ├── admin.py              # Configuração do admin
│   └── urls.py               # URLs do app
├── templates/                # Templates HTML
│   ├── base.html             # Template base
│   ├── registration/         # Templates de autenticação
│   └── relatorios/           # Templates do app
├── static/                   # Arquivos estáticos
├── media/                    # Uploads de arquivos
├── requirements.txt          # Dependências Python
├── Procfile                  # Configuração Render
├── build.sh                  # Script de build
├── .env.example              # Exemplo de variáveis
└── README.md                 # Este arquivo
```

## 🎯 Como Usar

### Para Usuários

1. **Login**: Acesse `/login/` com suas credenciais
2. **Dashboard**: Visualize todos os relatórios disponíveis
3. **Filtros**: Use a busca e filtros por tipo para encontrar relatórios
4. **Visualização**: Clique em "Ver" para detalhes do relatório
5. **Download**: Clique em "Download" para baixar o arquivo

### Para Administradores

1. **Acesse o Admin**: `/admin/` com credenciais de superusuário
2. **Gerenciar Usuários**: Crie e gerencie contas de usuário
3. **Gerenciar Relatórios**: Adicione, edite e remova relatórios
4. **Configurações**: Ajuste permissões e configurações do sistema

## 🔐 Tipos de Relatório

O sistema suporta os seguintes tipos de relatório:

- **Financeiro**: Relatórios financeiros e contábeis
- **Vendas**: Relatórios de vendas e performance comercial
- **Marketing**: Relatórios de campanhas e métricas de marketing
- **Operacional**: Relatórios operacionais e de processos
- **Recursos Humanos**: Relatórios de RH e gestão de pessoas
- **Outros**: Outros tipos de relatórios

## 🛡️ Segurança

- Autenticação obrigatória para acesso ao sistema
- Proteção CSRF em todos os formulários
- Configurações de segurança para produção
- Validação de uploads de arquivo
- Headers de segurança configurados

## 🔄 Atualizações

Para atualizar o sistema:

1. **Desenvolvimento Local**:
   ```bash
   git pull origin main
   pip install -r requirements.txt
   python manage.py migrate
   python manage.py collectstatic
   ```

2. **Produção (Render)**:
   - Faça push das alterações para o GitHub
   - O Render fará o redeploy automaticamente

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 🤝 Contribuição

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📞 Suporte

Para suporte ou dúvidas:

- Abra uma issue no GitHub
- Entre em contato com a equipe de desenvolvimento
- Consulte a documentação do Django: https://docs.djangoproject.com/

---

**Desenvolvido com ❤️ usando Django**

