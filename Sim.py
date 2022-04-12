from Mind import Mind
import pygame
from time import time
import random as rand

BLACK = (0, 0, 0)
GRAY = (127, 127, 127)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

numPeople = 100
maxX = 100
maxY = 50
maxMood = 255
multiplier = 10
offset = multiplier / 2
width = (maxX + 2) * multiplier
height = (maxY + 2) * multiplier
background = BLACK
lines = False

mind = Mind(numPeople, maxX, maxY, maxMood, multiplier)

pygame.init()
screen = pygame.display.set_mode((width, height))
caption = "Simulation"
pygame.display.set_caption(caption)

def peopleToPoints():
    points = []
    for person in mind.people:
        points.append(list(((person.loc.x * multiplier), (person.loc.y * multiplier), person.mood, person.id)))
    return points

points = peopleToPoints()
running = True
playing = False
epoch = 0

def move(epoch):
    mind.moveAll()
    points = peopleToPoints()
    return points

prev_move = time()
frame_delay = 0.05

def update(screen, points):
    screen.fill(background)
    for point in points:
        if lines:
            for id in mind.distances[point[3]].keys():
                x = mind.people[id].loc.x * multiplier
                y = mind.people[id].loc.y * multiplier
                pygame.draw.line(screen, GRAY, (point[0] + offset, point[1] + offset), (x + offset, y + offset))
        pygame.draw.rect(screen, (0, point[2], 255 - point[2]), (point[0], point[1], multiplier, multiplier))
    
    pygame.display.update()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                epoch += 1
                points = move(epoch)
            if event.key == pygame.K_p:
                playing = not playing
            if event.key == pygame.K_h:
                id = rand.randint(0, numPeople - 1)
                mind.people[id].mood = 255
                for neighbor in mind.distances[id]:
                    mind.people[neighbor].mood = 250
                points = peopleToPoints()
                update(screen, points)
            if event.key == pygame.K_s:
                id = rand.randint(0, numPeople - 1)
                mind.people[id].mood = 0
                for neighbor in mind.distances[id]:
                    mind.people[neighbor].mood = 5
                points = peopleToPoints()
                update(screen, points)
            if event.key == pygame.K_l:
                lines = not lines
    
    if playing:
        if time() - prev_move > frame_delay:
            epoch += 1
            points = move(epoch)
            prev_move = time()
    
    update(screen, points)

pygame.quit()