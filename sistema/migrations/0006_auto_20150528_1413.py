# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0005_auto_20150528_1311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='usuario',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, blank=True),
        ),
    ]
