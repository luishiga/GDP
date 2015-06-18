# -*- coding: utf-8 -*-
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from sistema.forms import *
from django.contrib.auth.decorators import login_required, permission_required
# Create your views here.
from datetime import date
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

# def criar_permissoes(request):
#     grupo_a = Group(name='administrador')
#     somemodel_ct = ContentType.objects.get(app_label='auth', model='user')
#     perm_g = Permission(name='Permissao gerente', codename='perm_g',content_type=somemodel_ct)
#     perm_c = Permission(name='Permissao coordenador', codename='perm_c',content_type=somemodel_ct)
#     g1 = Group(name='analista')
#     g2 = Group(name='gerente')
#     g3 = Group(name='coordenador')
#     lista = Funcionario.objects.all()
#     for u in lista:
#         if u.cargo == 'a':
#             u.group = [g1]
#         elif u.cargo == 'g':
#             u.group = [g2]
#         elif u.cargo == 'c':
#             u.group = [g3]
#         if u.usuario.is_superuser()==True:
#             u.group = [g1,g2,g3]
#     return redirect("/admin/")

def login_sistema (request):
    if request.method=="GET":
        login_form=LoginForm()
    else:
        login_form=LoginForm(request.POST)
        if login_form.is_valid():
            usuario = login_form.cleaned_data['username']
            senha = login_form.cleaned_data['password']
            user = authenticate(username=usuario, password=senha)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect("/home/")
                else:
                    messages.error(request, 'Este usuário não está ativo')
            else:
                messages.error(request, 'Este usuário e/ou senha não existe')
        else:
            messages.error(request, 'Confira o preenchimento dos campos abaixo')

    return render (request, "login.html",locals())

@login_required
def logout_sistema (request):
    logout(request)
    return redirect('/login/')

@login_required
def home(request):
    # if funcionario.usuario.senha == funcionario.email:
    #     alerta =
    usuario = request.user
    funcionario_corrente = Funcionario.objects.get(usuario=usuario)
    try:
        nfunc = Funcionario.objects.count()
    except:
        nfunc = 0
    try:
        nproj = Projeto.objects.count()
    except:
        nproj = 0
    c = funcionario_corrente.cargo
    if c == 'g' or c == 'a':
        projeto = funcionario_corrente.projeto
        lista_etapas = Etapas.objects.filter(projeto = projeto)
        for e in lista_etapas:
            lista_doc = Documentos.objects.filter(etapa = e)
            for d in lista_doc:
                if d.status =='1' and c =='g':
                    messages.warning(request, 'Você tem documento(s) a ser(em) avaliado(s)')
                    break
                elif d.status =='0' and c =='a':
                    messages.warning(request, 'Você tem documento(s) requisitado(s)')
                    break
    return render (request, "inicio.html",locals())


# cadastro do funcionario, sendo o usuario e senha igual ao email
@login_required
@permission_required('auth.perm_c', login_url='/home/')
def funcionario_cadastrar(request):
    funcionario_form = FuncionarioForm()
    contato_form = ContatoForm()
    if request.method == 'POST':
        funcionario_form = FuncionarioForm(request.POST)
        contato_form = ContatoForm(request.POST)
        if funcionario_form.is_valid() and contato_form.is_valid():
            email = contato_form.cleaned_data['email']
            try:
                usuario_existente = User.objects.get(email = email)
                messages.error(request, 'Este email já foi cadastrado')
            except:
                contato = contato_form.save()
                user = User.objects.create_user(username=email,email=email,password=email)
                user.save()
                funcionario = funcionario_form.save(commit = False)
                funcionario.usuario = user
                funcionario.contato = contato
                funcionario.cargo = 'u'
                funcionario.save()
                messages.success(request, 'Funcionário criado com sucesso!')
        else:
            messages.error(request, 'Confira o preenchimento dos dados')
    return render (request, "funcionario_cadastrar.html", locals())

@login_required
@permission_required('auth.perm_c', login_url='/home/')
def projeto_cadastrar(request):
    projeto_form = ProjetoForm()
    cliente_form = ClienteForm()
    contato_form = ContatoForm()
    if request.method == 'POST':
        projeto_form = ProjetoForm(request.POST)
        cliente_form = ClienteForm(request.POST)
        contato_form = ContatoForm(request.POST)
        if projeto_form.is_valid() and cliente_form.is_valid():
            projeto = projeto_form.save()
            criar_etapas(projeto.id)
            contato = contato_form.save()
            cliente = cliente_form.save(commit=False)
            cliente.projeto = projeto
            cliente.contato = contato
            cliente.save()
            messages.success(request, 'Projeto cadastrado com sucesso!')
            return redirect('/aloca_pessoa/%d/' % projeto.id)
        else:
            messages.error(request, 'Confira o preenchimento dos dados')
    return render (request, "projeto_cadastrar.html", locals())

def criar_etapas(id_projeto):
    projeto_corrente = Projeto.objects.get(id=id_projeto)
    etapa1 = Etapa.objects.create(nome="Modelo de Negócios",projeto=projeto_corrente)
    etapa2 = Etapa.objects.create(nome="Requisitos",projeto=projeto_corrente)
    etapa3 = Etapa.objects.create(nome="Análise e Design",projeto=projeto_corrente)
    etapa4 = Etapa.objects.create(nome="Implementação",projeto=projeto_corrente)
    etapa5 = Etapa.objects.create(nome="Teste",projeto=projeto_corrente)
    etapa6 = Etapa.objects.create(nome="Desenvolvimento",projeto=projeto_corrente)
    return

@login_required
@permission_required('auth.perm_c', login_url='/home/')
def pessoa_alocar(request, id_projeto):
    usuario = request.user
    funcionario_corrente = Funcionario.objects.get(usuario=usuario)
    cargo = funcionario_corrente.cargo
    projeto_corrente = Projeto.objects.get(id=id_projeto)
    equipe_atual = Funcionario.objects.filter(projeto=projeto_corrente)
    alocar_form = AlocarForm()
    if request.method == 'POST':
        alocar_form = AlocarForm(request.POST)
        if alocar_form.is_valid():
            limpa_equipe_atual(projeto_corrente.id)
            gerente = alocar_form.cleaned_data['gerente']
            gerente.projeto = projeto_corrente
            gerente.cargo = 'g'
            g1 = Group.objects.get(name='gerente')
            g1.user_set.add(gerente.usuario)
            analista1 = alocar_form.cleaned_data['analista1']
            analista1.projeto = projeto_corrente
            analista1.cargo = 'a'
            g2 = Group.objects.get(name='analista')
            g2.user_set.add(analista1.usuario)
            analista2 = alocar_form.cleaned_data['analista2']
            analista2.projeto = projeto_corrente
            analista2.cargo = 'a'
            g2.user_set.add(analista2.usuario)
            analista3 = alocar_form.cleaned_data['analista3']
            analista3.projeto = projeto_corrente
            analista3.cargo = 'a'
            g2.user_set.add(analista3.usuario)
            analista4 = alocar_form.cleaned_data['analista4']
            analista4.projeto = projeto_corrente
            analista4.cargo = 'a'
            g2.user_set.add(analista4.usuario)
            gerente.save()
            analista1.save()
            analista2.save()
            analista3.save()
            analista4.save()
            messages.success(request, "Pessoal alocado com sucesso!")
        else:
            messages.error(request, "Erro no envio de dados")
    return render(request, "pessoa_alocar.html", locals())

def limpa_equipe_atual(id_projeto):
    projeto_corrente = Projeto.objects.get(id=id_projeto)
    lista = Funcionario.objects.filter(projeto=projeto_corrente)
    g1 = Group.objects.get(name='gerente')
    g2 = Group.objects.get(name='analista')
    print("oi")
    for f in lista:
        print("nn")

        f.cargo = 'u'
        f.projeto = None
        u = f.usuario
        try:
            g1.user_set.remove(u)
        except:
            g2.user_set.remove(u)
        f.save()
    return

@login_required
@permission_required('auth.perm_a', login_url='/home/')
def projetos_listar(request):
    usuario = request.user
    funcionario_corrente = Funcionario.objects.get(usuario=usuario)
    cargo = funcionario_corrente.cargo
    lista = Projeto.objects.all()
    return render(request, "projetos.html", locals())

@login_required
@permission_required('auth.perm_a', login_url='/home/')
def projeto_ver(request, id_projeto):
    projeto_corrente = Projeto.objects.get(id = id_projeto)
    etapas = Etapa.objects.filter(projeto = projeto_corrente)
    return render(request, "projeto.html", locals())

@login_required
@permission_required('auth.perm_a', login_url='/home/')
def documentos_ver(request, id_projeto, id_etapa):
    projeto_corrente = Projeto.objects.get(id = id_projeto)
    etapa_corrente = Etapa.objects.get(id = id_etapa)
    documentos = Documento.objects.filter(etapa = etapa_corrente)
    lista = Documento.objects.filter(etapa = etapa_corrente)
    documento_form = DocumentoForm()
    return render(request,"documentos.html", locals())

@login_required
@permission_required('auth.perm_g', login_url='/home/')
def documento_requisitar(request, id_projeto, id_etapa):
    projeto_corrente = Projeto.objects.get(id = id_projeto)
    etapa_corrente = Etapa.objects.get(id = id_etapa)
    if request.method == 'POST':
        documento_form = DocumentoForm(request.POST)
        if documento_form.is_valid():
            documento = documento_form.save(commit=False)
            documento.data_criacao = date.today()
            documento.status = '0'
            documento.etapa = etapa_corrente
            documento.save()
            messages.success(request,"Documento requisitado")
        else:
            messages.error(request,"Confira o preenchimento do campo")
    return redirect('/projetos/%d/etapa/%d/' %(projeto_corrente.id,etapa_corrente.id))

@login_required
@permission_required('auth.perm_a', login_url='/home/')
def documento_escrever(request, id_projeto, id_etapa, id_documento):
    projeto_corrente = Projeto.objects.get(id = id_projeto)
    etapa_corrente = Etapa.objects.get(id = id_etapa)
    documento_corrente = Documento.objects.get(id = id_documento)
    documento_form = EscreverForm(instance=documento_corrente)
    if request.method == 'POST':
        documento_form = EscreverForm(request.POST)
        if documento_form.is_valid():
            texto_input = documento_form.cleaned_data['texto']
            documento_corrente.texto = texto_input
            documento_corrente.status = '1'
            documento_corrente.data_revisao = date.today()
            documento_corrente.save()
            messages.success(request,"Texto salvo")
        else:
            messages.error(request,"Confira o preenchimento do texto")
    return render(request,"documento_escrever.html", locals())

# permissao de gerente do projeto
@login_required
@permission_required('auth.perm_g', login_url='/home/')
def documento_avaliar(request, id_projeto, id_etapa, id_documento):
    documento_corrente = Documento.objects.get(id = id_documento)
    return render(request,"documento_avaliar.html", locals())

@login_required
@permission_required('auth.perm_g', login_url='/home/')
def documento_aprovar(request, id_projeto, id_etapa, id_documento):
    projeto_corrente = Projeto.objects.get(id = id_projeto)
    etapa_corrente = Etapa.objects.get(id = id_etapa)
    documento_corrente = Documento.objects.get(id = id_documento)
    documento_corrente.status = '2'
    documento_corrente.data_aprovacao = date.today()
    documento_corrente.save()
    return redirect('/projetos/%d/etapa/%d/' %(projeto_corrente.id,etapa_corrente.id))

@login_required
@permission_required('auth.perm_g', login_url='/home/')
def documento_reprovar(request, id_projeto, id_etapa, id_documento):
    projeto_corrente = Projeto.objects.get(id = id_projeto)
    etapa_corrente = Etapa.objects.get(id = id_etapa)
    documento_corrente = Documento.objects.get(id = id_documento)
    documento_corrente.status = '0'
    documento_corrente.data_aprovacao = date.today()
    documento_corrente.save()
    return redirect('/projetos/%d/etapa/%d/' %(projeto_corrente.id,etapa_corrente.id))
