#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  petle_cw3.py

def main(args):
	kwa = 0
    a = int(input("Podaj liczbę której mają się wyświetlać kwadraty: "))

    for a in range(a + 1):
		kwa = a * a
        print(kwa)

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
