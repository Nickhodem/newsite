# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scanning', '0003_page_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='quality',
            field=models.PositiveSmallIntegerField(default=1),
        ),
    ]
