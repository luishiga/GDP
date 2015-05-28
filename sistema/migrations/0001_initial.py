# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=128, verbose_name=b'Nome')),
                ('cargo', models.CharField(max_length=16, choices=[(b'c', b'Coordenador'), (b'g', b'Gerente'), (b'a', b'Analista'), (b'u', b'Usu\xc3\xa1rio')])),
                ('nivel_formacao', models.CharField(max_length=16, verbose_name=b'N\xc3\xadvel de Forma\xc3\xa7\xc3\xa3o', choices=[(b'0', b'T\xc3\xa9cnico'), (b'1', b'Superior Incompleto'), (b'2', b'Superior Completo'), (b'3', b'P\xc3\xb3s-Graduado'), (b'4', b'Outro')])),
                ('usuario', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Funcion\xe1rio',
                'verbose_name_plural': 'Funcion\xe1rios',
            },
        ),
    ]
