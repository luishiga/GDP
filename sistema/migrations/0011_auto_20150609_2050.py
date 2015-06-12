# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0010_auto_20150609_1916'),
    ]

    operations = [
        migrations.RenameField(
            model_name='documento',
            old_name='Etapa',
            new_name='etapa',
        ),
    ]
