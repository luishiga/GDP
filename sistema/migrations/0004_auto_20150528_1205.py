# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0003_auto_20150521_1324'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projeto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=128, verbose_name=b'Nome do Projeto ')),
                ('inicio', models.DateField(verbose_name=b'Data de cria\xc3\xa7\xc3\xa3o')),
                ('prazo', models.DateField(verbose_name=b'Prazo final')),
            ],
            options={
                'verbose_name': 'Projeto',
                'verbose_name_plural': 'Projetos',
            },
        ),
        migrations.AddField(
            model_name='contato',
            name='comercial',
            field=models.IntegerField(null=True, verbose_name=b'Telefone comercial'),
        ),
        migrations.AddField(
            model_name='contato',
            name='endereco',
            field=models.CharField(max_length=128, null=True, verbose_name=b'Endere\xc3\xa7o'),
        ),
        migrations.AddField(
            model_name='contato',
            name='residencial',
            field=models.IntegerField(null=True, verbose_name=b'Telefone residencial'),
        ),
        migrations.AlterField(
            model_name='contato',
            name='celular',
            field=models.IntegerField(null=True, verbose_name=b'Celular'),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='usuario',
            field=models.OneToOneField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='funcionario',
            name='projeto',
            field=models.ForeignKey(blank=True, to='sistema.Projeto', null=True),
        ),
    ]
