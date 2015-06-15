# -*- coding: utf-8 -*-
from django.forms import ModelForm, TextInput, Select, PasswordInput, Textarea, CharField
from django import forms
from sistema.models import *
from localflavor.br.forms import *

# Register your forms here.

class LoginForm(forms.Form):
    username = forms.CharField(max_length=64)
    password = forms.CharField(max_length=64, widget=forms.PasswordInput)

class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        exclude = ('contato','usuario', 'projeto',)

class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = '__all__'

class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = '__all__'

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        exclude = ('projeto', 'contato',)

class AlocarForm(forms.Form):
    gerente = forms.ModelChoiceField(queryset=Funcionario.objects.all().order_by('nome'))
    analista1 = forms.ModelChoiceField(queryset=Funcionario.objects.all().order_by('nome'))
    analista2 = forms.ModelChoiceField(queryset=Funcionario.objects.all().order_by('nome'))
    analista3 = forms.ModelChoiceField(queryset=Funcionario.objects.all().order_by('nome'))
    analista4 = forms.ModelChoiceField(queryset=Funcionario.objects.all().order_by('nome'))

class DocumentoForm(forms.ModelForm):
    class Meta:
        model = Documento
        fields = ('nome',)
