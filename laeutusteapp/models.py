__author__ = 'vaino'
from django.db import models

# Create your models here.
class Kohad(models.Model):
    ruum = models.CharField(max_length=100)
    kuup = models.DateTimeField('lisatud')

    def __unicode__(self):
        return self.ruum

    class Meta:
        verbose_name_plural = "Kohad"


class Liik(models.Model):
    nimetus = models.CharField(max_length=100)

    def __unicode__(self):
        return self.nimetus

    class Meta:
        verbose_name_plural = "Liigid"


class Asi(models.Model):
    nimetus = models.CharField(max_length=100)
    liik = models.ForeignKey(Liik)
    laenutusi = models.IntegerField(default=0)


    def __unicode__(self):
        return self.nimetus


    class Meta:
        verbose_name_plural = "riistvara"


class Kes(models.Model):
    nimi = models.CharField(max_length=100)
    epost = models.CharField(max_length=30, default='')

    def __unicode__(self):
        return self.nimi

    class Meta:
        verbose_name_plural = "Laenutuste lisajad"


class Laenutused(models.Model):
    asi = models.ForeignKey(Asi)
    kuup = models.DateTimeField('laenutuse aeg')
    ruum = models.ForeignKey(Kohad)
    kes = models.ForeignKey('Kes', default='')
    # def __unicode__(self):
    # 	return strftime(self.kuup)


    class Meta:
        verbose_name_plural = "Laenutused"
