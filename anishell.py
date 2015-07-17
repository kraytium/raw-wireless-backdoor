class map():
    def __init__(self, h, w):
         self.set = []
         self.height = h
         self.width = w
         self.depth = {}
         
         # create rows
         for y in range(h):
             self.set.append([])
             
         # create pixles
         for row in range(len(self.set)):
             for x in range(w):
                 self.set[row].append(' ')
                 
    def addSprite(self, sprite):
        # add sprite to set, check for errors
        if sprite.depth > len(self.depth):
            self.depth[len(self.depth)] = shape
         
        elif sprite.depth in self.depth:
            self.depth[len(self.depth)] = sprite
        
        else:
            self.depth[sprite.depth] = sprite

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
                                # if pixle is not ' ' set pixle on map
                                if not sprite.content[y-sprite.y][x-sprite.x] == ' ':
                                    self.set[y][x] = sprite.content[y-sprite.y][x-sprite.x]
 
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
                self.set[y][x] = ' '

class sprite():
    def __init__(self, content, name, y=0, x=0, depth=0):
        self.content = content
        self.name = name
        self.y = y
        self.x = x
        self.depth = depth
        
        # check if content is string
        if type(content) is str:
            self.content = strToArr(content)
        
        else:
            self.content = content
            
        # number of pixles in content, excluding space
        self.pixles = 0
        for row in content:
            for pixle in row:
                if not pixle == ' ':
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

def clear(): print chr(27) + '[2J'
