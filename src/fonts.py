
from font_data import asteroids, hershey

def draw_char(c, startx, starty, size=5, use_asteroids=True):
    if use_asteroids:
        font = asteroids
    else:
        font = hershey

    if c not in font:
        print ("'%s' not fond in font " % c)
        c = '?'

    scale = 3000
    ret = []

    cret = []
    lastfx = 0
    lastfy = 0

    maxx=startx
    maxy=starty
    ret=[]
    for pth in font[c]:

        pret = []
        for (px,py) in pth:
            x = startx + (px / scale * size)
            y = starty + (py / scale * size)
            maxx = max(maxx, x)
            maxy = max(maxy, y)
            pret.append((x,y))

        ret.append(pret)
        
    return ret, maxx,maxy

def draw_str(s, startx, starty, size=4, use_asteroids=False):
    paths =[]
    x = startx
    for c in s:
        cpaths, maxx, _ = draw_char(c, x, starty,size, use_asteroids=use_asteroids)
        x = maxx + 2/size
        paths.extend(cpaths)

    return paths

def draw_str_center(s, x, y, centery=False, centerx=False, alignright=False, size=4, use_asteroids=False):
    paths =[]

    maxx=0
    maxy=0
    for c in s:
        cpaths, maxx, ry = draw_char(c, maxx, 0, use_asteroids=use_asteroids)
        maxy=max(ry, maxy)
        maxx = maxx + 2/size

    if centerx:
        x = x - maxx/2
    if centery:
        y = y - maxy/2

    if alignright:
        x = x-maxx
        
    return draw_str(s, x,y, size, use_asteroids)
