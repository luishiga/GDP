# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0009_auto_20150609_1915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='etapa',
            name='inicio',
            field=models.DateField(null=True, verbose_name=b'Data de cria\xc3\xa7\xc3\xa3o', blank=True),
        ),
        migrations.AlterField(
            model_name='etapa',
            name='prazo',
            field=models.DateField(null=True, verbose_name=b'Prazo Final', blank=True),
        ),
    ]
