# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AnagraficheGenerali',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('ragsoc', models.CharField(max_length=75, verbose_name='Ragione Sociale')),
                ('cognome', models.CharField(null=True, max_length=50, verbose_name='Cogonome')),
                ('nome', models.CharField(null=True, max_length=50, verbose_name='Nome')),
                ('indirizzo', models.CharField(null=True, max_length=50, verbose_name='Indirizzo')),
                ('citta', models.CharField(null=True, max_length=50, verbose_name='Citta')),
                ('frazione', models.CharField(null=True, max_length=50, verbose_name='Frazione')),
                ('provincia', models.CharField(null=True, max_length=2, verbose_name='Provincia')),
                ('cap', models.CharField(null=True, max_length=5, verbose_name='CAP')),
                ('piva', models.CharField(null=True, max_length=12, verbose_name='Partita Iva')),
                ('codfisc', models.CharField(null=True, max_length=12, verbose_name='Codice Fiscale')),
                ('email', models.EmailField(null=True, max_length=75, verbose_name='E-mail')),
                ('emailpec', models.EmailField(null=True, max_length=75, verbose_name='E-mail pec')),
                ('internet', models.URLField(null=True, max_length=75, verbose_name='Sito web')),
                ('tel', models.CharField(null=True, max_length=15, verbose_name='Telefono')),
                ('fax', models.CharField(null=True, max_length=15, verbose_name='Fax')),
                ('cell', models.CharField(null=True, max_length=15, verbose_name='Cellulare')),
                ('utente', models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='Utente')),
            ],
            options={
                'verbose_name_plural': 'Anagrafica Generale',
            },
        ),
        migrations.CreateModel(
            name='Azienda',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('ragsoc', models.ForeignKey(to='tabgen.AnagraficheGenerali', verbose_name='Azienda')),
                ('utente', models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='Utente')),
            ],
            options={
                'verbose_name_plural': 'Azienda',
            },
        ),
    ]
