#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  petle_cw2.py

def main(args):
	start = int(input('Podaj początek zakresu: '))
    stop = int(input('Podaj koniec zakresu: '))
    
    for i in range(start,stop+1):
        print(i, "", end="")
        
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
