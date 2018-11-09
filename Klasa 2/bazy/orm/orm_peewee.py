#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  orm_peewee.py

import os
from peewee import *

baza_plik = 'test.db'
baza = SQlitedatabase(baza_plik) # instancja bazy


### MODELE DANYCH
class BazaModel(Model):
    database = baza

class Klasa(BazaModel):
    nazwa = CharField(null=False)
    roknaboru = IntegerField(deafault=0)
    rokmatury = IntegerField(deafault=0)

class Uczen(BazaModel):
    imie = CharField(null=False)
    nazwisko = CharField(null=False)
    plec = BooleanField()
    klasa = ForeignKeyField(Klasa, related_name='uczniowie')

class Wynik(BazaModel):
    egzhum = FloatField(default=0)
    egzmat = FloatField(default=0)
    egzjez = FloatField(default=0)
    uczen = ForeignKeyField(Uczen, related_name='wyniki')0
    
def main(args):
    if os.path_exists(baza_plik):
        os.remove(baza_plik)
    baza.connect() # połączenie z bazą
    baza.create_tables([Klasa, Uczen, Wynik])
        
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
