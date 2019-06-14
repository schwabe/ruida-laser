#! /usr/bin/python3

import ruida
from random import randint

from fonts import draw_str, draw_str_center

def getRGB():
    return (randint(0,255),randint(0,255),randint(0,255))



def main():
    max = 40
    r = ruida.Ruida()
    powers = (13,17,25,30,37,50)
    speeds = (100,75,50,25,12)
    nlayers=len(powers)*len(speeds)
    print("Num layer: %d" % nlayers)
    r.set(nlayers=min(nlayers,max))

    fontxoffset = 10
    fontyoffset = 4
    kasten=5
    lnum =0
    margin=0.75
    raster =2*margin+kasten
    for i,s in enumerate(speeds):
        for j,p in enumerate(powers):
          x = i*raster + fontxoffset + margin
          y = j*raster + fontyoffset + margin
          paths = [ [[x,y], [x+kasten,y], [x+kasten,y+kasten], [x, y+kasten], [x,y]] ]
          
          #layer = ruida.RuidaLayer(paths=paths, speed=[2000,s*10], power=p)

          if i == 1 and j == 1:
          # Beschriftung
              paths.extend(draw_str_center("spd", fontxoffset, 0, alignright=True))

              for bi,bs in enumerate(speeds):
                  xb = bi*raster + fontxoffset+raster/2
                  paths.extend(draw_str_center("%d" % bs, xb, 0, centerx=True))



              for bj,bp in enumerate(powers):
                  yb = bj*raster + fontyoffset + raster/2
                  paths.extend(draw_str_center("%d%%" % bp, fontxoffset, yb, centery=True, alignright=True))



          r.set(layer=lnum, speed=s, power=[p,p], color=getRGB(), paths=paths)
          lnum+=1
          

    with open("calib.rd", "wb") as out:
        r.write(out)

                        

if __name__=='__main__':
    main()
         
