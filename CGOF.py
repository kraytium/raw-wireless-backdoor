from anishell import *
from time import sleep
from random import randint

def genLife(h, w, den, l, d):
    map = []
    for y in range(h):
        map.append([])
        
        for x in range(w):
            if randint(1, int(1/den)) == 1:
                map[y].append(l)
                
            else:
                map[y].append(d)
                
    return map
    
live = 'O'
dead = ' '
all = genLife(26, 36, .15, live, dead)
cells = {}
y = len(all)

rows = []
for row in all:
            rows.append(len(row))
x = max(rows)

bg = map(y, x)

for row in range(y):
    for cell in range(x):
        if all[row][cell] == live:
                    
            cells[row, cell] = sprite(live, (row, cell), y=row, x=cell)
            bg.addSprite(cells[row, cell])
            
        else:
            cells[row, cell] = sprite(dead,  (row, cell), y=row, x=cell)
        
for n in range(1600):
    #sleep(.1)
    clear()
    print bg.render()
    
    for row in range(y):
        for cell in range(x):
            if cells[row, cell].content[0][0] == live:
                if (len(bg.getTouching(sprite=cells[row, cell])) < 2) or (len(bg.getTouching(sprite=cells[row, cell])) > 3):
                    bg.removeSprite(cells[row, cell])
                    cells[row, cell].content[0][0] = dead
                    
            else:
                if len(bg.getTouching(pixle=(row, cell))) == 3:
                    bg.addSprite(cells[row, cell])
                    cells[row, cell].content[0][0] = live
