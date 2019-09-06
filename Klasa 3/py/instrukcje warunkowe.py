#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  instrukcje warunkowe.py
#  



def main(args):
    a = int(input("Podaj pierwszą liczbę: "))
    b = int(input("Podaj drugą liczbę: "))
    c = int(input("Podaj trzecią liczbę: "))
    d = 0
    print(a, b, c)
    if a>b and a>c:
        d=a
    elif b>a and b>c:
        d=b
    elif c>a and c>b:
        d=c
    print ("Największa liczba to: ", d)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
