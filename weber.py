import pygame
import random
import math
import sys

width = 1200 
height = 800
numDots = 100
black = 0, 0, 0
tick = 2

class Dot():
    def __init__(self):
        self.x = random.randint(0, width)
        self.y = random.randint(0, height)
        self.r = 1 
    
class Square():
    def __init__(self, dots):
        self.dots = dots

def draw_dots(numDots, surface):
    dots = []
    while len(dots) < numDots:
        new = Dot()
        if any(pow(d.r - new.r, 2) <=
            pow(d.x - new.x, 2) + pow(d.y - new.y, 2) <=
            pow(d.r + new.r, 2)
            for d in dots):
                continue

        dots.append(new)
        pygame.draw.circle(surface, black, (new.x, new.y), new.r, 0)
        pygame.display.update()

    pygame.event.clear()
    done = False
    while not done:
        event = pygame.event.wait()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1: 
                print("You pressed 1")
                done = True
            elif event.key == pygame.K_2:
                print("You pressed 2")
                done = True

if __name__ == '__main__':
    pygame.init()

    screen = pygame.display.set_mode([width, height])
    screen.fill((255, 255, 255))

    pygame.display.set_caption("Weber's Law on Vision")

    squares = []
    draw_dots(numDots, screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Quitting")
                pygame.quit()
                sys.exit()


