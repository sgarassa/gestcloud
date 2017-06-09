# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('tabgen', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Strutture',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('categoria', models.CharField(null=True, max_length=15, verbose_name='Categoria')),
                ('latitudine', models.CharField(null=True, max_length=15, verbose_name='Latitudine')),
                ('longitudine', models.CharField(null=True, max_length=15, verbose_name='longitudine')),
                ('perapert', models.CharField(null=True, max_length=35, verbose_name='Periodi di Apertura')),
                ('servgen', models.CharField(null=True, max_length=50, verbose_name='Servizi Generici')),
                ('servcam', models.CharField(null=True, max_length=50, verbose_name='Servizi in camera')),
                ('prezzoalst', models.CharField(null=True, max_length=50, verbose_name='Prezzo alta stagione')),
                ('prezzomedst', models.CharField(null=True, max_length=50, verbose_name='Prezzo media stagione')),
                ('prezzobasst', models.CharField(null=True, max_length=50, verbose_name='Prezzo bassa stagione')),
                ('azienda', models.ForeignKey(to='tabgen.Azienda', verbose_name='Azienda')),
                ('ragsoc', models.ForeignKey(to='tabgen.AnagraficheGenerali', verbose_name='Denominazione')),
            ],
            options={
                'verbose_name_plural': 'Strutture',
            },
        ),
        migrations.CreateModel(
            name='TipoStrut',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('descrizione', models.CharField(max_length=50, verbose_name='Descrizione')),
                ('azienda', models.ForeignKey(to='tabgen.Azienda', verbose_name='Azienda')),
            ],
            options={
                'verbose_name_plural': 'Tipologia Struttura',
            },
        ),
        migrations.AddField(
            model_name='strutture',
            name='tipologia',
            field=models.ForeignKey(to='crm.TipoStrut', verbose_name='Tipologia'),
        ),
        migrations.AddField(
            model_name='strutture',
            name='utente',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='Utente'),
        ),
    ]
