from django.db import models

class Jenerator(models.Model):
        Ricardo = "Ricardo"
        Dongfeng = "Dongfeng"
        Baudouin ="Baudouin"
        Deutz = "Deutz"
        Perkins = "Perkins"
        ENGINE_CHOICES = [
        (Ricardo,"Ricardo"),
        (Dongfeng ,"Dongfeng"),
        (Baudouin,"Baudouin"),
        (Deutz, "Deutz"),
        (Perkins, "Perkins"),

                          ]

        engine = models.CharField(max_length=15,choices=ENGINE_CHOICES,default=Ricardo,verbose_name='Motor')
        jenModel = models.CharField(max_length=10, null=True, verbose_name='Model')
        kva = models.CharField(max_length=10, null=True, verbose_name= 'KVa' )
        frekans = models.CharField(max_length=10, null=True, verbose_name='Frekans')
        fiyat = models.CharField(max_length=15, null=True, verbose_name='Fiyat')
        katalogTr = models.FileField(null=True, verbose_name='DataSheet TR')
        katalogEn = models.FileField(null=True, verbose_name='DataSheet EN')
        photo = models.FileField(null=True, verbose_name='Photo')
   