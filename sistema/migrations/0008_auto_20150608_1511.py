# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0007_auto_20150528_1422'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projeto',
            old_name='nome',
            new_name='nome_projeto',
        ),
        migrations.AlterField(
            model_name='cliente',
            name='nome',
            field=models.CharField(max_length=128, verbose_name=b'Nome do Cliente'),
        ),
        migrations.AlterField(
            model_name='documento',
            name='nome',
            field=models.CharField(max_length=128, verbose_name=b'Nome do Documento'),
        ),
        migrations.AlterField(
            model_name='etapa',
            name='nome',
            field=models.CharField(max_length=128, verbose_name=b'Nome da Etapa'),
        ),
    ]
