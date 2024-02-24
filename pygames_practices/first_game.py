import pygame, sys

pygame.init()

patanlla=pygame.display.set_mode((600, 500))
tittle=pygame.display.set_caption("Mi primer juego")

#Colores
Blanco=(255, 255, 255)
Negro=(0, 0, 0)
Rojo=(245, 9, 13)
Azul=(9, 16, 245)
Verde=(12, 150, 3)

patanlla.fill(Blanco)

rectangulo=pygame.draw.rect(patanlla, Rojo, (300, 300, 200, 150))
linea=pygame.draw.line(patanlla, Negro, (100, 150), (200, 100), 10)
circulo=pygame.draw.circle(patanlla, Azul, (400, 200), 40, 0)


#Bucle
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.update()
