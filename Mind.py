import math
import random as rand
from Person import Person
from Point import Point

class Mind:
    def __init__(self, numPeople, maxX, maxY, maxMood, multiplier, seed = None):
        self.numPeople = numPeople
        self.maxX = maxX
        self.maxY = maxY
        self.maxMood = maxMood
        self.multiplier = multiplier
        self.radius = round(math.sqrt(maxX**2 + maxY**2) / 10, 1)

        if seed != None:
            rand.seed(seed)
        
        self.people = []

        for i in range(self.numPeople):
            self.people.append(Person(i, Point(rand.randint(1, self.maxX), rand.randint(1, self.maxY)), rand.randint(0, self.maxMood)))
        
        self.calculateDistances()

    def calculateDistances(self):
        self.distances = {i:{} for i in range(self.numPeople)}

        for i in range(self.numPeople):
            for j in range(i + 1, self.numPeople):
                a = self.people[i]
                b = self.people[j]
                dist = a.distance(b)
                if dist <= self.radius:
                    if len(self.distances[a.getId()]) > 4:
                        test = self.distances[a.getId()]
                        maxDistIndex = self.findMaxDistIndex(test)
                        if dist < self.distances[a.getId()][maxDistIndex]:
                            self.distances[a.getId()].pop(maxDistIndex)
                            self.distances[a.getId()][b.getId()] = dist
                    else:
                        self.distances[a.getId()][b.getId()] = dist
                    if len(self.distances[b.getId()]) > 4:
                        maxDistIndex = self.findMaxDistIndex(self.distances[b.getId()])
                        if dist < self.distances[b.getId()][maxDistIndex]:
                            self.distances[b.getId()].pop(maxDistIndex)
                            self.distances[b.getId()][a.getId()] = dist
                    else:
                        self.distances[b.getId()][a.getId()] = dist
    
    def printPeople(self):
        for person in self.people:
            print(person.print())
    
    def printDistances(self):
        for person in self.distances:
            print(self.distances[person])

    def findMaxDistIndex(self, dict):
        maxIndex = 0
        currMax = 0
        currIndex = -1
        for val in dict:
            currIndex = val
            if dict[val] > currMax:
                currMax = dict[val]
                maxIndex = currIndex 
        return maxIndex

    def moveAll(self):
        for person in self.people:
            validChoices = self.getValidChoices(person)
            move = rand.choice(validChoices)
            person.move(move[0], move[1])
        self.calculateDistances()
        self.updateMoods()
    
    def updateMoods(self):
        for person in self.people:
            id = person.getId()
            closestTotal = 0
            for neighbor in self.distances[id].keys():
                closestTotal += self.people[neighbor].mood
            if closestTotal != 0:
                average = int(closestTotal / len(self.distances[id].keys()))
                percentAverage = int(abs(average - person.mood) / 10)
                if average > person.mood:
                    person.mood = person.mood + percentAverage
                elif average < person.mood:
                    person.mood = person.mood - percentAverage

    def getValidChoices(self, person):
        x = person.loc.x
        y = person.loc.y
        choices = []
        for i in range(4):
            choices.append([0, 0])
        if ((y-1)*self.multiplier) > 0:
            choices.append([0, -1])
        if ((y+1) <= self.maxY):
            choices.append([0, 1])
        if ((x-1)*self.multiplier) > 0:
            choices.append([-1, 0])
        if ((x+1) <= self.maxX):
            choices.append([1, 0])
        return choices
