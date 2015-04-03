# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('h2h', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='matches',
            name='m_id',
        ),
    ]
