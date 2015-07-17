# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('watering', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='suburb',
            name='comment',
            field=models.CharField(max_length=512, null=True),
            preserve_default=True,
        ),
    ]
