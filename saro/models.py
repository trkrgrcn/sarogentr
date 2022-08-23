from tkinter import Widget
from django.db import models

class Contact(models.Model):
    adSoyad = models.CharField(max_length=250, verbose_name='Ad Soyad')
    eMail = models.EmailField(verbose_name='Email')
    firmaAdi = models.CharField(max_length=200, verbose_name='Firma Adı')
    telefon = models.CharField(max_length=20, verbose_name='Telefon' )
    adres = models.CharField(max_length=200,verbose_name='Adres')
    konu = models.CharField(max_length=100, verbose_name='Konu')
    mesaj = models.TextField(verbose_name='Mesajınız')



