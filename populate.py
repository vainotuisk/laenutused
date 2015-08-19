import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'laenutused.settings.development')

import django
django.setup()

from laeutusteapp.models import Kohad, Liik, Asi, Kes, Laenutused
from django.utils import timezone
def populate():
    add_koht(ruum='arvutiklass',kuup=timezone.now())
    add_koht(ruum='kantselei',kuup=timezone.now())
    add_koht(ruum='1-1',kuup=timezone.now())
    add_koht(ruum='2-3',kuup=timezone.now())
    add_liik(nimetus='arvuti')
    add_liik(nimetus='tahvel')
    add_asi(nimetus='a001',liik=Liik.objects.get(id=1),laenutusi=3)
    add_asi(nimetus='a002',liik=Liik.objects.get(id=1),laenutusi=2)
    add_asi(nimetus='t001',liik=Liik.objects.get(id=2),laenutusi=30)
    add_asi(nimetus='t002',liik=Liik.objects.get(id=2),laenutusi=13)
    add_asi(nimetus='t003',liik=Liik.objects.get(id=2),laenutusi=3)
    add_kes(nimi='Juku',epost='juku@adress.com')
    add_kes(nimi='Mann',epost='mann@adress.com')
    add_kes(nimi='Sekretar',epost='sekr@adress.com')
    add_laenutus(asi=Asi.objects.get(id=1),kuup=timezone.now(),ruum=Kohad.objects.get(id=1),kes=Kes.objects.get(id=1))
    add_laenutus(asi=Asi.objects.get(id=2),kuup=timezone.now(),ruum=Kohad.objects.get(id=2),kes=Kes.objects.get(id=2))
    for c in Kohad.objects.all():
        print str(c)
def add_koht(ruum,kuup):
    p = Kohad.objects.get_or_create(ruum=ruum,kuup=kuup)[0]
    p.save()
    return p
def add_liik(nimetus):
    p = Liik.objects.get_or_create(nimetus=nimetus)[0]
    p.save()
    return p
def add_asi(nimetus,liik,laenutusi):
    p = Asi.objects.get_or_create(nimetus=nimetus,liik=liik,laenutusi=laenutusi)[0]
    p.save()
    return p
def add_kes(nimi,epost):
    p = Kes.objects.get_or_create(nimi=nimi,epost=epost)[0]
    p.save()
    return p
def add_laenutus(asi,kuup,ruum,kes):
    p = Laenutused.objects.get_or_create(asi=asi,kuup=kuup,ruum=ruum,kes=kes)[0]
    p.save()
    return p
# def add_asi(nimetus,liik,laenutusi):
#     p = Asi.objects.get_or_create(nimetus=nimetus,liik=liik,laenutusi=laenutusi)[0]
#     p.save()
#     return p
if __name__ == '__main__':
    print "Alustan andmete lisamist"
    populate()
