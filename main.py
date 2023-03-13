import pygame
import random
import sys

r = 200

total = 0
circle = 0

width = r*2
height = r*2

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Pi Day Monte Carlo Estimation')

pygame.draw.circle(screen, 255, (width//2, height//2), r)

while True:
    for _ in range(1000):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        x = random.uniform(-r, r)
        y = random.uniform(-r, r)
        total += 1
        if x*x+y*y < r*r:
            pygame.draw.circle(screen, (250, 12, 226), (width//2 + x, height//2 + y), 1)
            circle += 1
        else:
            pygame.draw.circle(screen, (12, 250, 250), (width//2 + x, height//2 + y), 1)

        pygame.display.update()

    pi = 4*(circle/total)
    print(pi)
