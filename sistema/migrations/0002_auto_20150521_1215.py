# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('celular', models.IntegerField(verbose_name=b'Celular')),
                ('email', models.EmailField(max_length=254, verbose_name=b'Email')),
            ],
            options={
                'verbose_name': 'Contato',
                'verbose_name_plural': 'Contatos',
            },
        ),
        migrations.AddField(
            model_name='funcionario',
            name='contato',
            field=models.ForeignKey(to='sistema.Contato', null=True),
        ),
    ]
