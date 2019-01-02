#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  algorytm02.py

def main(args):
    n = int(input("Liczba: "))
    silnia = 1
    i = 1
    while i <= n:
        silnia * i
        print(silnia)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
