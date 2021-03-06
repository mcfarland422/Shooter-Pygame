import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self,screen):
        super(Bullet, self).__init__()
        self.screen = screen

        self.rect = pygame.Rect(0,0,5,20)
        self.color = (0,0,0)

    def update(self):
        if self.direction == 1: #up
            self.y -= self.speed #change the y, each time update is run, by bullet speed
            self.rect.y = self.y #update rect position
        elif self.direction == 2: #right
            self.x += self.speed #change the y, each time update is run, by bullet speed
            self.rect.x = self.x #update rect position
        elif self.direction == 3: #down
            self.y += self.speed #change the y, each time update is run, by bullet speed
            self.rect.y = self.y #update rect position
        else: #left
            self.x -= self.speed #change the y, each time update is run, by bullet speed
            self.rect.x = self.x #update rect position
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect) #draw the bullet!
