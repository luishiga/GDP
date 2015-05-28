# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0002_auto_20150521_1215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='contato',
            field=models.OneToOneField(null=True, to='sistema.Contato'),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='nivel_formacao',
            field=models.CharField(max_length=16, verbose_name=b'N\xc3\xadvel de forma\xc3\xa7\xc3\xa3o', choices=[(b'0', b'T\xc3\xa9cnico'), (b'1', b'Superior Incompleto'), (b'2', b'Superior Completo'), (b'3', b'P\xc3\xb3s-Graduado'), (b'4', b'Outro')]),
        ),
    ]
