# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('addclass', '0002_auto_20171025_0816'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='price',
        ),
    ]
