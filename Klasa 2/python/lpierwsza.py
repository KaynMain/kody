#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  lpierwsza.py
#

def main(args):
    n = int(input("Podaj liczbę: "))
    i = 2
    while i * i <= n:
        if n % 1 == 0:
            print("Złożona")
            return 0
        i += 1
    print("Pierwsza")
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
