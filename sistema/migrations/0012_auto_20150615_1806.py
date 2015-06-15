# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0011_auto_20150609_2050'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gerente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.AlterField(
            model_name='documento',
            name='data_aprovacao',
            field=models.DateField(null=True, verbose_name=b'Data de aprova\xc3\xa7\xc3\xa3o', blank=True),
        ),
        migrations.AlterField(
            model_name='documento',
            name='data_revisao',
            field=models.DateField(null=True, verbose_name=b'Data de revis\xc3\xa3o', blank=True),
        ),
        migrations.AlterField(
            model_name='documento',
            name='texto',
            field=models.TextField(null=True, verbose_name=b'Detalhamento', blank=True),
        ),
    ]
