import pygame
class Gun():
    def __init__(self,screen):
        """using gun for first level"""
        self.screen = screen
        self.image = pygame.image.load('image/images/1663762805_b-3.jpg')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.center = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom
        self.mright = False
        self.mleft = False

    def output(self):
        """painting gun"""
        self.screen.blit(self.image,self.rect)