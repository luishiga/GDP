# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0014_projeto_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projeto',
            name='inicio',
            field=models.DateField(null=True, verbose_name=b'Data de cria\xc3\xa7\xc3\xa3o'),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='prazo',
            field=models.DateField(null=True, verbose_name=b'Prazo final'),
        ),
    ]
