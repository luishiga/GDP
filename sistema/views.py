# -*- coding: utf-8 -*-
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from sistema.forms import *

# Create your views here.


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

def logout_sistema (request):
    logout(request)
    return redirect('/login/')


def home(request):
    # if funcionario.usuario.senha == funcionario.email:
    #     alerta =
    return HttpResponse("Welcome home!")

# cadastro do funcionario, sendo o usuario e senha igual ao email

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
                funcionario.user = user
                funcionario.contato = contato
                return H
                funcionario.save()
                messages.success(request, 'Funcionário criado com sucesso!')
        else:
            messages.error(request, 'Confira o preenchimento dos dados')
    return render (request, "funcionario_cadastrar.html", locals())

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
            contato = contato_form.save()
            cliente = cliente_form.save(commit=False)
            cliente.projeto = projeto
            cliente.contato = contato
            cliente.save()
            messages.success(request, 'Projeto cadastrado com sucesso!')
            return HttpResponse("OK")
            # return redirect('/alocar_pessoa/{{projeto.id}}')
        else:
            messages.error(request, 'Confira o preenchimento dos dados')
    return render (request, "projeto_cadastrar.html", locals())

def pessoa_alocar(request, id_projeto):
    projeto_corrente = Projeto.objects.get(id=id_projeto)
    equipe_atual = Funcionario.objects.filter(projeto=projeto_corrente)
    alocar_form = AlocarForm()
    if request.method == 'POST':
        alocar_form = AlocarForm(request.POST)
        if alocar_form.is_valid():
            gerente = alocar_form.cleaned_data['gerente']
            gerente.projeto = projeto_corrente
            gerente.cargo = 'g'
            analista1 = alocar_form.cleaned_data['analista1']
            analista1.projeto = projeto_corrente
            analista2 = alocar_form.cleaned_data['analista2']
            analista2.projeto = projeto_corrente
            analista3 = alocar_form.cleaned_data['analista3']
            analista3.projeto = projeto_corrente
            analista4 = alocar_form.cleaned_data['analista4']
            analista4.projeto = projeto_corrente
            gerente.save()
            analista1.save()
            analista2.save()
            analista3.save()
            analista4.save()
            messages.success(request, "Pessoal alocado com sucesso!")
        else:
            messages.error(request, "Erro no envio de dados")
    return render(request, "pessoa_alocar.html", locals())

# def documento_requisitar():

# def documento_avaliar():

# def documento_aprovar():

# def documento_reprovar():

# def revisao_requisitar():

# def documento_criar():

# def documento_editar():

