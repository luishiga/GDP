# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0008_auto_20150608_1511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='etapa',
            name='inicio',
            field=models.DateField(verbose_name=b'Data de cria\xc3\xa7\xc3\xa3o', blank=True),
        ),
        migrations.AlterField(
            model_name='etapa',
            name='prazo',
            field=models.DateField(verbose_name=b'Prazo Final', blank=True),
        ),
    ]
