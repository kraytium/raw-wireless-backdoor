from anishell import sprite, map, clear
from time import sleep

ship = '123\n | \nabc'

test = sprite(ship, 'dux')
test2 = sprite(ship, 'cockies', x=20, y=9)
bg = map(15, 26)
bg.addSprite(test)
bg.addSprite(test2)

#while True:
for i in range(15):
    test.x = i+1
    
    test2.y = i+1
    
    clear()
    print 'test y, x: ' + str(test.y) + ', ' + str(test.x)
    print  'test2 y, x: ' + str (test2.y) + ', ' + str(test2.x)
    print bg.render()
    sleep(.5)