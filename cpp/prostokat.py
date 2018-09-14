#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  prostokat.py


def obwod(a, b):
    return 2 *a + 2 * b

def pole(a, b):
    return a * b
    
    
def main(args):
    a = int(input("Podaj pierwszy bok: "))
    b = int(input("Podaj drugi bok: "))
    print(a, b)
    
    print("Obwód prostokąta: ", obwod(a, b))
    print("Pole prostokąta: ", pole(a, b))
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
