import pygame, sys

def events(screen , assss):
    """making event"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            #right
            if event.key == pygame.K_RIGHT:
                assss.mright = True
            elif event.key == pygame.K_LEFT:
                assss.mleft = True
        elif event.type == pygame.KEYUP:
            #right
            if event.key == pygame.K_RIGHT:
                assss.mright = False
            elif event.key == pygame.K_LEFT:
                assss.mleft = False
def update(bg_color, screen ,assss):
    """updating screen"""
    screen.fill(bg_color)

    assss.output()
    pygame.display.flip()