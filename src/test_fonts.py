#! /usr/bin/python3

import ruida
from random import randint
import fonts

def getRGB():
    return (randint(0,255),randint(0,255),randint(0,255))



def main():
    max = 40
    r = ruida.Ruida()
    r.set(nlayers=1)

    lnum =0


    paths = []
    x=0
    y=0
    for i in range(ord(' '), ord('z')):
        c = chr(i)
        cpaths, maxx = fonts.draw_char(c, x, y, use_asteroids=False)
        x = maxx + 1

        paths.extend(cpaths)


    r.set(layer=0, speed=100, power=[20,20], color=getRGB(), paths=paths)
    with open("test_fonts.rd", "wb") as out:
        r.write(out)

if __name__=='__main__':
    main()
