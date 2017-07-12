from __future__ import unicode_literals
from django.db import models

NEW = (
    ('NEW', 'NEW'),
    ('NOTNEW', 'NOTNEW'),
)

CAT = (
    ('bracelets', 'bracelets'),
    ('kettingen', 'kettingen'),
)

SUBCAT = (
    ('leather', 'leather'),
    ('sil_bal', 'Silver Balled'),
    ('sil_chain', 'Silver Chained'),
    ('beads', 'Beads'),
)

# Create your models here.

class bp_pages(models.Model):
    pagina = models.CharField(max_length=200)
    inhoud = models.TextField()
    over_ons = models.TextField()

    class Meta:
        verbose_name = 'Pagina'
        verbose_name_plural = 'Paginas'

class bp_products(models.Model):
    pr_naam = models.CharField(max_length=200)
    pr_beschrijving = models.TextField()
    pr_cat = models.CharField(max_length=200, choices=CAT)
    pr_subcat= models.CharField(max_length=200, choices=SUBCAT)
    pr_prijs = models.IntegerField()
    file = models.ImageField()
    datestamp = models.DateTimeField(auto_now_add=True)
    new = models.CharField(max_length=50, choices=NEW)

    def __unicode__(self):
       return self.pr_naam

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Producten'

class bp_users(models.Model):
    voornaam = models.CharField(max_length=200)
    achternaam = models.CharField(max_length=200)
    straat = models.CharField(max_length=200)
    nummer = models.IntegerField()
    postcode = models.CharField(max_length=200)
    plaats = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

    def __unicode__(self):
       return self.voornaam


    class Meta:
        verbose_name = 'Gebruikers'
        verbose_name_plural = 'Gebruikers'

class ContactModel(models.Model):
    voornaam = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    onderwerp = models.CharField(max_length=200)
    text = models.TextField()

    def __unicode__(self):
        return self.onderwerp

    class Meta:
        verbose_name = 'Contactformulier'
        verbose_name_plural = 'Contactformulier'


