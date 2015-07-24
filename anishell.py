class map():
    def __init__(self, h, w, bgChar=' '):
         self.set = []
         self.height = h
         self.width = w
         self.bgChar = bgChar
         self.depth = []
         
         # create rows
         for y in range(h):
             self.set.append([])
             
         # create pixles
         for row in range(len(self.set)):
             for x in range(w):
                 self.set[row].append(self.bgChar)
                 
         # set pixle-sprite reference
         self.pixleRef = {}
                 
    def addSprite(self, sprite):
        # add sprite to set, check for errors
        if sprite.depth-1 > len(self.depth):
            self.depth.append(sprite)
            
        elif sprite.depth-1 < 0:
            self.depth.insert(0, sprite)
        
        else:
            self.depth.insert(sprite.depth-1, sprite)

    def removeSprite(self, sprite):
        # remove sprite from map
        self.depth.remove(sprite)
        
    def render(self, returnType='string'):
        # create and return pixle map
        # clear the screen
        self.clear()      
       
        # loop through sprites, if pixles from sprite share
        # the same location with a  sprite with a depth of a
        # higher value the sprite's pixle will get overwriten
        for z in range(len(self.depth)-1, -1, -1):
            sprite = self.depth[z]
            
            # loop through rows, check if sprite has a row in the map
            for y in range(len(self.set)):
                if (y-sprite.y > -1) and (y-sprite.y < len(sprite.content)):
                    # loop through pixles, check if sprite has pixle in the row
                    for x in range(len(self.set[y])):
                        if (x-sprite.x > -1) and (x-sprite.x < len(sprite.content[y-sprite.y])):
                            if sprite.content[y-sprite.y][x-sprite.x]:
                                # if pixle is not bgChar set pixle on map
                                if not sprite.content[y-sprite.y][x-sprite.x] == sprite.bgChar:
                                    self.set[y][x] = sprite.content[y-sprite.y][x-sprite.x]
                                    self.pixleRef[y, x] = sprite
 
        # choose whether to return map as array or string
        if returnType == 'string':
            string = ''
        
            for row in self.set:
                for pixle in row:
                    string += pixle
                
                string += '\n'
                
            return string.rstrip('\n')
            
        else:
        
            return self.set
           
    def clear(self):
        # clear the screen
        for y in range(len(self.set)):
            for x in range(len(self.set[y])):
                self.set[y][x] = self.bgChar
                
        # clear the pixle-sprite reference
        self.pixleRef = {}
                
    def getTouching(self, sprite='', pixle=''):
        # get list of sprites touching this sprite
        touching = []
        
        if sprite:
            for row in range(len(sprite.content)):
                for pixle in range(len(sprite.content[row])):
                    if not sprite.content[row][pixle] == sprite.bgChar:
                        for yOffset in [-1, 0, 1]:
                            for xOffset in [-1, 0, 1]:
                                y = sprite.y+row+yOffset
                                x = sprite.x+pixle+xOffset
                            
                                if (y, x) in self.pixleRef:
                                    if (not self.pixleRef[y, x] in touching) and (self.pixleRef[y, x] != sprite):
                                        touching.append(self.pixleRef[y, x])

        else:
            for yOffset in [-1, 0, 1]:
                for xOffset in [-1, 0, 1]:
                    y = pixle[0]+yOffset
                    x = pixle[1]+xOffset
                    
                    if (y, x) in self.pixleRef:
                        if not self.pixleRef[y, x] in touching:
                            touching.append(self.pixleRef[y, x])

        return touching

class sprite():
    def __init__(self, content, name, y=0, x=0, depth=0, bgChar='.'):
        self.content = content
        self.name = name
        self.y = y
        self.x = x
        self.depth = depth
        self.bgChar = bgChar
        
        # check if content is string
        if type(content) is str:
            self.content = strToArr(content)
        
        else:
            self.content = content
            
        # number of pixles in content, excluding space
        self.pixles = 0
        for row in content:
            for pixle in row:
                if not pixle == self.bgChar:
                    self.pixles += 1
             
        # total dimensions of content
        rows = []
        for row in content:
            rows.append(len(row))
        self.size = len(content)*max(rows)

def strToArr(str):
    # converts a string to pixle map array
    arr = []
    for row in str.split('\n'):
        arr.append([])
        for pixle in row:
            arr[-1].append(pixle)

    return arr

def clear():
    # clear the screen
    print chr(27) + '[2J'
