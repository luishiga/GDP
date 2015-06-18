# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0012_auto_20150615_1806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documento',
            name='data_aprovacao',
            field=models.DateField(null=True, verbose_name=b'Data de avalia\xc3\xa7\xc3\xa3o', blank=True),
        ),
        migrations.AlterField(
            model_name='documento',
            name='data_criacao',
            field=models.DateField(verbose_name=b'Data de requisi\xc3\xa7\xc3\xa3o'),
        ),
        migrations.AlterField(
            model_name='documento',
            name='data_revisao',
            field=models.DateField(null=True, verbose_name=b'\xc3\x9altima modifica\xc3\xa7\xc3\xa3o', blank=True),
        ),
    ]
