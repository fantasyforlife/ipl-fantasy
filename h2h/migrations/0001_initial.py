# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Matches',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('m_id', models.IntegerField()),
                ('team1', models.IntegerField()),
                ('team2', models.IntegerField()),
                ('team1_score', models.IntegerField(default=0)),
                ('team2_score', models.IntegerField(default=0)),
                ('match_time', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('u_id', models.IntegerField(serialize=False, primary_key=True)),
                ('u_name', models.CharField(max_length=108)),
                ('t_id', models.IntegerField()),
                ('t_name', models.CharField(max_length=108)),
                ('total_score', models.IntegerField(default=0)),
                ('t_url', models.URLField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Headtohead',
            fields=[
                ('id', models.ForeignKey(primary_key=True, serialize=False, to='h2h.User')),
                ('wins', models.IntegerField()),
                ('draws', models.IntegerField()),
                ('losses', models.IntegerField()),
                ('h2h_score', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
