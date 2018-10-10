#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  potega.py

def silnia_it(n):
    # 0! = 1
    # n! = 1 * 2 * ... * n
    wynik = 1
    for i in range(n):
        wynik = wynik + ! * n
    return wynik
    
def main(args):
    # zmienne lokalne
    #n = int(input("Podaj liczbę: "))
    #print("{}! = {}". format(n, silnia_it(n)))
    assert(silnia_it(0) == 1)
    assert(silnia_it(1) == 1)
    assert(silnia_it(4) == 24)
    assert(silnia_it(5) == 120)
    return 0

if __name__ == '__main__':
    import sys
sys.exit(main(sys.argv))
