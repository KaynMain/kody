#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  algorytm01.py


def wesja1():
    n = int(input("Liczba: "))
    i = 1
    for i in range(1, n, 2):
        print(i)
        
def wesja2():
    n = int(input("Liczba: "))
    i = 1
    while i < n:
        print(i)
        i += 2
        
def main(args):
    wersja2()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
