# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='asi',
            name='liik',
        ),
        migrations.RemoveField(
            model_name='laenutused',
            name='asi',
        ),
        migrations.RemoveField(
            model_name='laenutused',
            name='kes',
        ),
        migrations.RemoveField(
            model_name='laenutused',
            name='ruum',
        ),
        migrations.DeleteModel(
            name='Asi',
        ),
        migrations.DeleteModel(
            name='Kes',
        ),
        migrations.DeleteModel(
            name='Kohad',
        ),
        migrations.DeleteModel(
            name='Laenutused',
        ),
        migrations.DeleteModel(
            name='Liik',
        ),
    ]
