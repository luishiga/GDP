# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0013_auto_20150618_0249'),
    ]

    operations = [
        migrations.AddField(
            model_name='projeto',
            name='status',
            field=models.BooleanField(default=False, verbose_name=b'Conclu\xc3\xaddo'),
        ),
    ]
