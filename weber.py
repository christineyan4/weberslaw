import pygame
import sys
import random
import math

WIDTH = 600
HEIGHT = 600

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class Dot():
    def __init__(self, square):
        self.x = random.randint(square.leftx + 2, square.rightx - 2)
        self.y = random.randint(square.topy + 2, square.bottomy - 2)
        self.r = 1

class Square():
    def __init__(self, leftx, rightx):
        self.leftx = leftx
        self.rightx = rightx
        self.topy = 200
        self.bottomy = 450
        self.rect = pygame.rect.Rect((leftx, 200), (250, 250))

def draw_squares(screen):
    squareone = Square(0, 250)
    squaretwo = Square(350, 600)
    pygame.draw.rect(screen, WHITE, squareone.rect)
    pygame.draw.rect(screen, WHITE, squaretwo.rect)
    pygame.display.update()

    return [squareone, squaretwo]

def draw_dots(numDots, square, screen):
    dots = []
    while len(dots) < numDots:
        new = Dot(square)
        if any(pow(d.r - new.r, 2) <=
            pow(d.x - new.x, 2) + pow(d.y - new.y, 2) <=
            pow(d.r + new.r, 2)
            for d in dots):
                continue
        
        dots.append(new)
        pygame.draw.circle(screen, BLACK, (new.x, new.y), new.r, 0)

def check_normal(accuracy):
    tentrials = accuracy[-10:]
    print(tentrials)

    diffsum = 0
    valsum = 0
    for (diff, value) in tentrials:
        diffsum += diff
        valsum += value

    print(valsum / 10)
    if 0.48 < valsum / 10 < 0.52:
        return diffsum / 10
    return None

def weber(numDots, squares, screen):
    diff = 1
    accuracy = []
    normalized = None
    trials = 0

    while not normalized:
        moredots = random.randint(0, 1)
        lessdots = 1 - moredots
        draw_dots(numDots + diff, squares[moredots], screen)
        draw_dots(numDots, squares[lessdots], screen)
        # add some text like, "Which box has more dots? Press 1 for left, 2 for right"

        pygame.display.update()
        
        if moredots == 0:
            correct = pygame.K_1
            wrong = pygame.K_2
        else:
            correct = pygame.K_2
            wrong = pygame.K_1

        pygame.event.clear()
        done = False
        while not done:
            event = pygame.event.wait()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == correct:
                    accuracy.append((diff, 1))
                    if diff != 1:
                        diff -= 1
                    done = True
                elif event.key == wrong:
                    accuracy.append((diff, 0))
                    diff += 1
                    done = True
        print(accuracy)
        trials += 1

        if trials >= 20:
            normalized = check_normal(accuracy)
            print(normalized)

        draw_squares(screen)
    
    print("NORMALIZED")
    return normalized

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode([WIDTH, HEIGHT])
    pygame.display.set_caption("Weber's Law on Vision")
    screen.fill(BLACK)
    results = {}

    #for numDots in range(10, 100, 10):
    for numDots in range(20, 100, 10):
        squares = draw_squares(screen)
        perceived = weber(numDots, squares, screen)
        results[numDots] = perceived
    print(results)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit() 