# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('class_management', '0002_auto_20171024_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='theuser',
            name='user_email',
            field=models.EmailField(max_length=75),
            preserve_default=True,
        ),
    ]
