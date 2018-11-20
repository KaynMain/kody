#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  kwadraty.py

import turtle

def rysujKwadrat(zolw, bok, ile):
    #for i in range(4):
    zolw.forward(bok)
    zolw.right(90)
    if ile > 0:
        rysujKwadrat(zolw, bok, ile-1)

def rysujKwadrat2(zolw, bok):
    for i in range(4):
        zolw.forward(bok)
        zolw.right(90)
    if bok > 0:
        rysujKwadrat2(zolw, bok-10)

def rysuj(zolw, bok, kat, warunek):
    zolw.forward(bok)
    zolw.right(kat)
    if kat < warunek:
        rysuj(zolw, bok, kat, warunek)    
    
def main(args):
    turtle.title("Kwadraty")
    turtle.setup(1000, 800)
    
    zolw = turtle.Turtle()
    zolw.color('black', 'yellow')
    zolw.pensize(2)
    zolw.speed(0)
    
    #rysujKwadrat(zolw, 100, 4)
    zolw.begin_fill()
    #rysujKwadrat2(zolw, 200)
    zolw.end_fill()
    rysuj(zolw, 50, 60, 180)
    
    turtle.done()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
