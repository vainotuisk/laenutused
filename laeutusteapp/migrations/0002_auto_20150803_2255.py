# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('laeutusteapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='kes',
            options={'verbose_name_plural': 'Kes'},
        ),
        migrations.AlterModelOptions(
            name='liik',
            options={'verbose_name_plural': 'Liigid'},
        ),
    ]
