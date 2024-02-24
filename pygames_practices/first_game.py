import pygame, sys

pygame.init()

patanlla=pygame.display.set_mode((600, 500))
tittle=pygame.display.set_caption("Mi primer juego")

while True:
    for event in pygame.event.get():
        if event.type == quit:
            pygame.quit()
            sys.exit()
