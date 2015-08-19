# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asi',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nimetus', models.CharField(max_length=100)),
                ('laenutusi', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Kes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nimi', models.CharField(max_length=100)),
                ('epost', models.CharField(default=b'', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Kohad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ruum', models.CharField(max_length=100)),
                ('kuup', models.DateTimeField(verbose_name=b'lisatud')),
            ],
        ),
        migrations.CreateModel(
            name='Laenutused',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('kuup', models.DateTimeField(verbose_name=b'laenutuse aeg')),
                ('asi', models.ForeignKey(to='accounts.Asi')),
                ('kes', models.ForeignKey(default=b'', to='accounts.Kes')),
                ('ruum', models.ForeignKey(to='accounts.Kohad')),
            ],
        ),
        migrations.CreateModel(
            name='Liik',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nimetus', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='asi',
            name='liik',
            field=models.ForeignKey(to='accounts.Liik'),
        ),
    ]
