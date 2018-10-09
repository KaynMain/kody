#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  liczby 2-3.py

def liczby2():
    """
    Drukuje wszytskie liczby dwucyfrowe o niepowtarzających się cyfrach z podanego zakresu oraz zwraca ilość takich liczb.
    Nie drukujemy: 11, 22, 33, 44, itd.
    """
    pass

def liczby3():
    """
    Drukuje wszytskie liczby trzycyfrowe o niepowtarzających się cyfrach z podanego zakresu oraz zwraca ilość takich liczb.
    Nie drukujemy: 111, 222, 112, 323, itd.
    """
    pass
        
def main(args):
    print(liczby2(11, 99))
    print(liczby3(100, 999))

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
