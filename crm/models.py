from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.conf import settings
from django.db import models
import tabgen

# Create your models here.

class TipoStrut(models.Model):
    azienda = models.ForeignKey(tabgen.models.Azienda, verbose_name='Azienda')
    descrizione = models.CharField(max_length=50, verbose_name='Descrizione')
    def __unicode__(self):
            return str(self.descrizione)
    class Meta:
            verbose_name_plural = 'Tipologia Struttura'

class Strutture(models.Model):
    azienda = models.ForeignKey(tabgen.models.Azienda, verbose_name='Azienda')
    utente = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Utente')
    ragsoc = models.ForeignKey(tabgen.models.AnagraficheGenerali, verbose_name='Denominazione')
    tipologia = models.ForeignKey(TipoStrut, verbose_name='Tipologia')
    categoria = models.CharField(max_length=15, null=True, verbose_name='Categoria')
    latitudine = models.CharField(max_length=15, null=True, verbose_name='Latitudine')
    longitudine = models.CharField(max_length=15, null=True, verbose_name='longitudine')
    perapert = models.CharField(max_length=35, null=True, verbose_name='Periodi di Apertura')
    servgen = models.CharField(max_length=50, null=True, verbose_name='Servizi Generici')
    servcam = models.CharField(max_length=50, null=True, verbose_name='Servizi in camera')
    prezzoalst = models.CharField(max_length=50, null=True, verbose_name='Prezzo alta stagione')
    prezzomedst = models.CharField(max_length=50, null=True, verbose_name='Prezzo media stagione')
    prezzobasst = models.CharField(max_length=50, null=True, verbose_name='Prezzo bassa stagione')
    def __unicode__(self):
            return str(self.ragsoc)
    class Meta:
            verbose_name_plural = 'Strutture'

