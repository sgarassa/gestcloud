from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

class AnagraficheGenerali(models.Model):
    utente = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Utente')
    ragsoc = models.CharField(max_length=75, verbose_name='Ragione Sociale')
    cognome = models.CharField(max_length=50, null=True, verbose_name='Cogonome')
    nome = models.CharField(max_length=50, null=True, verbose_name='Nome')
    indirizzo = models.CharField(max_length=50, null=True, verbose_name='Indirizzo')
    citta = models.CharField(max_length=50,null=True, verbose_name='Citta')
    frazione = models.CharField(max_length=50,null=True, verbose_name='Frazione')
    provincia = models.CharField(max_length=2,null=True, verbose_name='Provincia')
    cap = models.CharField(max_length=5,null=True, verbose_name='CAP')
    piva = models.CharField(max_length=12,null=True, verbose_name='Partita Iva')
    codfisc = models.CharField(max_length=12, null=True, verbose_name='Codice Fiscale')
    email = models.EmailField(max_length=75, null=True, verbose_name='E-mail')
    emailpec = models.EmailField(max_length=75, null=True, verbose_name='E-mail pec')
    internet = models.URLField(max_length=75, null=True, verbose_name='Sito web')
    tel = models.CharField(max_length=15, null=True, verbose_name='Telefono')
    fax = models.CharField(max_length=15, null=True, verbose_name='Fax')
    cell = models.CharField(max_length=15, null=True, verbose_name='Cellulare')
    def __unicode__(self):
            return str(self.ragsoc)
    class Meta:
            verbose_name_plural = 'Anagrafica Generale'

class Azienda(models.Model):
    utente = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Utente')
    ragsoc = models.ForeignKey(AnagraficheGenerali, verbose_name='Azienda')
    def __unicode__(self):
            return str(self.ragsoc)
    class Meta:
            verbose_name_plural = 'Azienda'

