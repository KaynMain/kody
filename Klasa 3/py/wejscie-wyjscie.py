#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  wejscie-wyjscie.py
#

def main(args):
    imie = input("Podaj swoje imię: ")
    nazwisko = input("Podaj swoje nazwisko: ")
    
    print("Witaj", imie, nazwisko)
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
