# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('laeutusteapp', '0003_auto_20150803_2300'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='kes',
            options={'verbose_name_plural': 'Laenutuste lisajad'},
        ),
    ]
