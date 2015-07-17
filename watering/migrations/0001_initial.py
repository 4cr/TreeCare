# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('account_num', models.CharField(max_length=32)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Suburb',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WateringSession',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('count', models.IntegerField(default=0)),
                ('genus', models.CharField(max_length=250)),
                ('volume', models.IntegerField(default=0)),
                ('location', models.CharField(max_length=250)),
                ('location_type', models.CharField(max_length=64)),
                ('frequency', models.CharField(max_length=32)),
                ('is_done', models.BooleanField(default=False)),
                ('account', models.ForeignKey(to='watering.Account')),
                ('suburb', models.ForeignKey(to='watering.Suburb')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
