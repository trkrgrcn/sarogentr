# Generated by Django 3.2.7 on 2022-08-18 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jenerator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('engine', models.CharField(choices=[('RC', 'Ricardo'), ('DF', 'Dongfeng'), ('BD', 'Baudouin'), ('DZ', 'Deutz'), ('PR', 'Perkins')], default='RC', max_length=2, verbose_name='Motor')),
                ('jenModel', models.CharField(max_length=10, verbose_name='Model')),
                ('kva', models.CharField(max_length=10, verbose_name='KVa')),
                ('frekans', models.CharField(max_length=10, verbose_name='Frekans')),
                ('fiyat', models.CharField(max_length=15, verbose_name='Fiyat')),
                ('katalogTr', models.FileField(upload_to='', verbose_name='DataSheet')),
                ('katalogEn', models.FileField(upload_to='', verbose_name='DataSheet')),
                ('photo', models.ImageField(upload_to='', verbose_name='Photo')),
            ],
        ),
    ]