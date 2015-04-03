# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('h2h', '0002_remove_matches_m_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='matches',
            name='m_id',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
    ]
