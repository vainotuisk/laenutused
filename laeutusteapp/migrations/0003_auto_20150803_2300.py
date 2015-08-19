# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('laeutusteapp', '0002_auto_20150803_2255'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='asi',
            options={'verbose_name_plural': 'riistvara'},
        ),
        migrations.AlterModelOptions(
            name='kohad',
            options={'verbose_name_plural': 'Kohad'},
        ),
        migrations.AlterModelOptions(
            name='laenutused',
            options={'verbose_name_plural': 'Laenutused'},
        ),
    ]
