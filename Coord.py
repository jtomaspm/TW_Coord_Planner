import math

class Coord:

    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)
    
    def __init__(self, c):
        s = c.split("|")
        self.x = int(s[0])
        self.y = int(s[1])

    def distance(self, coord):
        coordA = [self.x, self.y]
        coordB = [coord.x, coord.y]
        distance = round(math.sqrt( ((int(coordA[0])-int(coordB[0]))**2)+((int(coordA[1])-int(coordB[1]))**2) ),1)
        return distance
    
    def above(self, coord):
        return (self.y < coord.y)

    def under(self, coord):
        return (self.y > coord.y)

    def left(self, coord):
        return (self.x < coord.x)

    def right(self, coord):
        return (self.x > coord.x)