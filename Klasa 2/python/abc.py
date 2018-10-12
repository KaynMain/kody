#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  abc.py
#
#  Program pobiera trzy liczby od użytkownika, a następnie wyświetla liczbę największą. 
#

def maks(a, b, c):
    m = None
    if a > b:
        if a > c:
            m = a
    elif b > c:
            m = b
    print ("Największa: ", m)
    return m
    

def maks2(a, b, c):
    """
    Funkcja wyszukuje i zwraca największą z trzecg podanych liczb
    """
    
    m = a
    if b > m:
        m = b
    if c > m:
        m = c
    return m
    
    
def main(args):
    assert(maks2(3, 2, 1) == 3)
    assert(maks2(2, 3, 1) == 3)
    assert(maks2(1, 2, 3) == 3)
    assert(maks2(1, 1, 3) == 3)
    assert(maks2(3, 1, 1) == 3)
    assert(maks2(1, 3, 1) == 3)
    assert(maks2(1, 3, 3) == 3)
    assert(maks2(3, 3, 1) == 3)
    assert(maks2(3, 3, 3) == 3)

    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
