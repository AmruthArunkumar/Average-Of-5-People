import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def setX(self, val):
        self.x = val
    
    def setY(self, val):
        self.y = val
    
    def distance(self, target):
        dx = target.x - self.x
        dy = target.y - self.y
        return round(math.sqrt(dx**2 + dy**2), 1)

    def print(self):
        return (self.x, self.y)