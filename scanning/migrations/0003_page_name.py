# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scanning', '0002_auto_20150628_0759'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='name',
            field=models.CharField(default='skaner', max_length=128),
            preserve_default=False,
        ),
    ]
