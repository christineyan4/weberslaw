import pygame
import random
import math

width = 1000 
height = 1000
numDots = 10
black = 0, 0, 0
tick = 2

class Dot():
    def __init__(self):
        self.x = random.randint(0, width)
        self.y = random.randint(0, height)
        self.r = 5 
    
class Square():
    def __init__(self, dots):
        self.dots = dots

if __name__ == '__main__':
    pygame.init()

    screen = pygame.display.set_mode([width, height])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    screen.fill((255, 255, 255))

    dots = []
    while len(dots) < numDots:
        new = Dot()
        if any(pow(d.r - new.r, 2) <=
            pow(d.x - new.x, 2) + pow(d.y - new.y, 2) <=
            pow(d.r + new.r, 2)
            for d in dots):
                continue

        dots.append(new)
        pygame.draw.circle(screen, black, (new.x, new.y), new.r, tick)
        pygame.display.update()

