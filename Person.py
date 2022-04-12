from Point import Point

class Person:
    def __init__(self, id, location:Point, mood):
        self.id = id
        self.loc = location
        self.mood = mood
    
    def getLoc(self):
        return self.loc

    def getMood(self):
        return self.mood
    
    def getId(self):
        return self.id
    
    def move(self, dx, dy):
        self.loc.setX(self.loc.getX() + dx)
        self.loc.setY(self.loc.getY() + dy)

    def distance(self, other):
        return self.loc.distance(other.getLoc())
    
    def print(self):
        return "Id: " + str(self.id) + " Location: " + str(self.loc.print()) + " Mood: " + str(self.mood)

