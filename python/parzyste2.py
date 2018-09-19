#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  parzyste.py



def main(args):
    start = int(input("Podaj liczbe początkową zakresu: "))
    stop = int(input("Podaj liczbe końcową zakresu: "))
    
    while start >= stop:
        stop = int(input("Podaj liczbe większą niż pierwsza: "))
    
    for liczba in range(start, stop + 1):
        #if liczba % 2 == 0:
        if not liczba % 2:
            print(liczba)
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
