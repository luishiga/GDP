# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
cargos = (
    ('c', 'Coordenador'),
    ('g', 'Gerente'),
    ('a', 'Analista'),
    ('u', 'Usuário'),
)

niveis_formacao = (
    ('0', "Técnico"),
    ('1', "Superior Incompleto"),
    ('2', "Superior Completo"),
    ('3', "Pós-Graduado"),
    ('4', "Outro"),
)

status_etapa = (
    ('0', "Planejada"),
    ('1', "Em progresso"),
    ('2', "Concluída")
)

status_documento = (
    ('0', "Requisitado"),
    ('1', "A avaliar"),
    ('2', "Aprovado")
)


class Projeto(models.Model):

    nome_projeto = models.CharField("Nome do Projeto ", max_length=128)
    inicio = models.DateField("Data de criação", null = True)
    prazo = models.DateField("Prazo final", null = True)
    status = models.BooleanField("Concluído", default = False, blank = True)
    class Meta:
        verbose_name = "Projeto"
        verbose_name_plural = "Projetos"

    def __unicode__(self):
        return self.nome_projeto

class Contato(models.Model):

    residencial = models.IntegerField("Telefone residencial", null = True)
    comercial = models.IntegerField("Telefone comercial", null = True)
    celular = models.IntegerField("Celular", null = True)
    email = models.EmailField("Email")
    endereco = models.CharField("Endereço", max_length=128, null = True)

    class Meta:
        verbose_name = "Contato"
        verbose_name_plural = "Contatos"

    def __unicode__(self):
        return self.email

class Funcionario(models.Model):

    nome = models.CharField("Nome", max_length=128)
    contato = models.OneToOneField(Contato, null = True) #null não é salvo no BD e blank não é requerido no form
    cargo = models.CharField(max_length=16, choices = cargos)
    nivel_formacao = models.CharField("Nível de formação", max_length=16, choices = niveis_formacao)
    usuario = models.OneToOneField(User, blank = True, null=True)
    projeto = models.ForeignKey(Projeto, blank = True, null = True)

    class Meta:
        verbose_name = "Funcionário"
        verbose_name_plural = "Funcionários"

    def __unicode__(self):
        return self.nome

class Gerente(models.Model):
    """docstring for Gerente"""
    def __init__(self, arg):
        super(Gerente, self).__init__()
        self.arg = arg


class Cliente(models.Model):

    nome = models.CharField("Nome do Cliente", max_length=128)
    contato = models.OneToOneField(Contato)
    projeto = models.OneToOneField(Projeto)

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def __unicode__(self):
        return self.nome


class Etapa(models.Model):

    nome = models.CharField("Nome da Etapa", max_length=128)
    inicio = models.DateField("Data de criação", blank=True, null=True)
    prazo = models.DateField("Prazo Final", blank=True, null=True)
    status = models.CharField(max_length=16, choices = status_etapa)
    projeto = models.ForeignKey(Projeto)

    class Meta:
        verbose_name = "Etapa"
        verbose_name_plural = "Etapas"

    def __unicode__(self):
        return self.nome + ' - ' + self.projeto.nome_projeto

class Documento(models.Model):

    nome = models.CharField("Nome do Documento", max_length=128)
    data_criacao = models.DateField("Data de requisição")
    status = models.CharField(max_length=16, choices = status_documento)
    data_revisao = models.DateField("Última modificação", blank=True, null=True)
    data_aprovacao = models.DateField("Data de avaliação", blank=True, null=True)
    texto = models.TextField("Detalhamento", blank=True, null=True)
    etapa = models.ForeignKey(Etapa)

    class Meta:
        verbose_name = "Documento"
        verbose_name_plural = "Documentos"

    def __unicode__(self):
        return self.nome
