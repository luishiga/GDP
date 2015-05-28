# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0004_auto_20150528_1205'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=128, verbose_name=b'Nome')),
                ('contato', models.OneToOneField(to='sistema.Contato')),
                ('projeto', models.OneToOneField(to='sistema.Projeto')),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
            },
        ),
        migrations.CreateModel(
            name='Documento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=128, verbose_name=b'Nome')),
                ('data_criacao', models.DateField(verbose_name=b'Data de cria\xc3\xa7\xc3\xa3o')),
                ('status', models.CharField(max_length=16, choices=[(b'0', b'Requisitado'), (b'1', b'A avaliar'), (b'2', b'Aprovado')])),
                ('data_revisao', models.DateField(verbose_name=b'Data de revis\xc3\xa3o')),
                ('data_aprovacao', models.DateField(verbose_name=b'Data de aprova\xc3\xa7\xc3\xa3o')),
                ('texto', models.TextField(verbose_name=b'Detalhamento')),
            ],
            options={
                'verbose_name': 'Documento',
                'verbose_name_plural': 'Documentos',
            },
        ),
        migrations.CreateModel(
            name='Etapa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=128, verbose_name=b'Nome')),
                ('inicio', models.DateField(verbose_name=b'Data de cria\xc3\xa7\xc3\xa3o')),
                ('prazo', models.DateField(verbose_name=b'Prazo Final')),
                ('status', models.CharField(max_length=16, choices=[(b'0', b'Planejada'), (b'1', b'Em progresso'), (b'2', b'Conclu\xc3\xadda')])),
                ('projeto', models.ForeignKey(to='sistema.Projeto')),
            ],
            options={
                'verbose_name': 'Etapa',
                'verbose_name_plural': 'Etapas',
            },
        ),
        migrations.AddField(
            model_name='documento',
            name='Etapa',
            field=models.ForeignKey(to='sistema.Etapa'),
        ),
    ]
