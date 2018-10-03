#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  prostokat-z-gwiazdek.py
#  Dane wejściowe: boki a i b prostokąta
#  Dane wyjściowe: prostokąt narywsowany w terminalu gwiazdkami o rozmiarach podancyh przez użytkownika 

def main(args):
    
    a = int(input("Podaj długość boku a: "))
    b = int(input("Podaj długość boku b: "))
    znak = input("Podaj znak którym chcesz rysować: ")
    
    for i in range(a):
        for j in range(b):
            print(znak, end = '')
        print()
        
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
