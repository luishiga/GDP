"""GDP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from sistema import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', views.login_sistema),
    url(r'^logout/$', views.logout_sistema),
    url(r'^home/$', views.home),   # a ser implementada
    url(r'^cadastra_funcionario/$', views.funcionario_cadastrar),
    url(r'^cadastra_projeto/$', views.projeto_cadastrar),
    url(r'^aloca_pessoa/(?P<id_projeto>[0-9]+)/$', views.pessoa_alocar),
    url(r'^projetos/$', views.projetos_listar),
    url(r'^projetos/(?P<id_projeto>[0-9]+)/$', views.projeto_ver),
    #url(r'^teste/(?P<id_projeto>[0-9]+)/$', views.criar_etapas),
    url(r'^projetos/(?P<id_projeto>[0-9]+)/etapa/(?P<id_etapa>[0-9]+)/$', views.documentos_ver),
    url(r'^projetos/(?P<id_projeto>[0-9]+)/etapa/(?P<id_etapa>[0-9]+)/requisita_documento/', views.documento_requisitar),
    # url(r'^avalia_documento/', views.documento_requisitar),
    # url(r'^aprova_documento/', views.documento_requisitar),
    # url(r'^reprova_documento/', views.documento_requisitar),
    # url(r'^requisita_documento/', views.documento_requisitar),
    # url(r'^cria_documento/', views.documento_requisitar),
    # url(r'^edita_documento/', views.documento_requisitar),

]
