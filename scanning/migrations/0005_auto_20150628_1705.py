# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scanning', '0004_page_quality'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tachymeter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=128)),
                ('name', models.CharField(max_length=128)),
                ('url', models.URLField()),
                ('quality', models.PositiveSmallIntegerField(default=1)),
                ('views', models.IntegerField(default=0)),
                ('likes', models.IntegerField(default=0)),
                ('category', models.ForeignKey(to='scanning.Category')),
            ],
        ),
        migrations.AddField(
            model_name='page',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
