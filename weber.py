import pygame
import random
import math
import sys

WIDTH = 1200 
HEIGHT = 800
numDots = 100
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class Dot():
    def __init__(self):
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(0, HEIGHT)
        self.r = 1 
    
"""
class Square():
    def __init__(self, x, y):
        self.x
        self.y
"""

def draw_squares(screen):
    squareone = pygame.rect.Rect(0, 0, WIDTH / 2, HEIGHT)
    squaretwo = pygame.rect.Rect(WIDTH / 2, 0, WIDTH / 2, HEIGHT) 
    squares = [squareone, squaretwo] 

    pygame.draw.rect(screen, BLACK, squareone, 1)
    pygame.draw.rect(screen, BLACK, squaretwo, 1)
    return squares

def draw_dots(numDots, square):
    dots = []
    while len(dots) < numDots:
        new = Dot()
        if any(pow(d.r - new.r, 2) <=
            pow(d.x - new.x, 2) + pow(d.y - new.y, 2) <=
            pow(d.r + new.r, 2)
            for d in dots):
                continue

        dots.append(new)
        pygame.draw.circle(square, BLACK, (new.x, new.y), new.r, 0)
        pygame.display.update()

def weber(squares):
    draw_dots(numDots, squares[0])
    draw_dots(numDots, squares[1])

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

    screen = pygame.display.set_mode([WIDTH, HEIGHT])
    screen.fill((255, 255, 255))

    pygame.display.set_caption("Weber's Law on Vision")

    squares = draw_squares(screen)
    
    weber(squares)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Quitting")
                pygame.quit()
                sys.exit()


