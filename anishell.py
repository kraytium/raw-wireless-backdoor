class set():
    def __init__(self, h, w):
         self.set = []
         self.height = h
         self.width = w
         self.depth = {}
         
         for y in range(h):
             self.set.append([])
             
         for row in range(len(self.set)):
             for x in range(w):
                 self.set[row].append(' ')
                 
    def addShape(self, shape):
        if shape.depth > len(self.depth):
            self.depth[len(self.depth)] = shape
            
        elif shape.depth in self.depth:
            self.depth[len(self.depth)+1] = shape
        
        else:
            self.depth[shape.depth] = shape

    def render(self, returnType='string'):
        for z in range(len(self.depth)-1, -1, -1):
            shape = self.depth[z]
            
            for y in range(len(self.set)):
                if (y-shape.y > -1) and (y-shape.y < len(shape.content)-1):
                    for x in range(len(self.set[y])):
                        if (x-shape.x > -1) and (x-shape.x < len(shape.content[y-shape.y])):
                            if shape.content[y-shape.y][x-shape.x]:
                                if not shape.content[y-shape.y][x-shape.x] == ' ':
                                    self.set[y][x] = shape.content[y-shape.y][x-shape.x]

        if returnType == 'string':
            string = ''
        
            for row in self.set:
                for pixle in row:
                    string += pixle
                
                string += '\n'
                
            return string.rstrip('\n')
            
        else:
        
            return self.set


class shape():
    def __init__(self, content, name, y=0, x=0, depth=0):
        self.content = content
        self.name = name
        self.y = y
        self.x = x
        self.depth = depth
        
        self.pixles = 0
        for row in content:
            for pixle in row:
                if not pixle == ' ':
                    self.pixles += 1
             
        rows = []
        for row in content:
            rows.append(len(row))
        self.size = len(content)*max(rows)