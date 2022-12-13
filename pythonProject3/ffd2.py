import pygame,controls
from pygame.locals import *
from asss import Penetration

pygame.init()
#у меня экран на компе маленьки поэтому такое разрешение:(
screen = pygame.display.set_mode((700 , 600))
#задание имени*
pygame.display.set_caption("fisting slave or zombotron")
#хз зачем это если потом фон, но пусть будет
bg_color = (0,0 ,0)
assss = Penetration(screen)
#загрузка фона*
slave_new_year = pygame.image.load('image/1663762805_b-3.jpg')

while True:
    controls.events(screen, assss)

    controls.update(bg_color, screen, assss)

run = True
while run:
#рисовка жесткого фона*

    screen.blit(slave_new_year, (0,0))
    #defolt body of program
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
pygame.quit()