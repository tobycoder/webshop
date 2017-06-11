from __future__ import unicode_literals

from django.db import models

# Create your models here.

class bp_pages(models.Model):
    pagina = models.CharField(max_length=200)
    inhoud = models.TextField()
    over_ons = models.TextField()

class bp_products(models.Model):
    pr_naam = models.CharField(max_length=200)
    pr_beschrijving = models.TextField()
    pr_cat = models.CharField(max_length=200)
    pr_subcat= models.CharField(max_length=200)
    pr_prijs = models.IntegerField()
    pr_image = models.CharField(max_length=200)
    datestamp = models.DateTimeField(auto_now_add=True)
    new = models.CharField(max_length=50)

    def __unicode__(self):
       return self.pr_naam

class bp_users(models.Model):
    voornaam = models.CharField(max_length=200)
    achternaam = models.CharField(max_length=200)
    straat = models.CharField(max_length=200)
    nummer = models.IntegerField()
    postcode = models.CharField(max_length=200)
    plaats = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

class ContactModel(models.Model):
    voornaam = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    onderwerp = models.CharField(max_length=200)
    text = models.TextField()
    def __unicode__(self):
        return self.onderwerp

class ShopCart(models.Model):
    name = models.CharField(max_length=200)
    q = models.IntegerField()
    maat = models.CharField(max_length=200)
    price = models.IntegerField()
