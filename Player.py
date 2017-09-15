import pygame
from pygame.sprite import Sprite

class Player(pygame.Sprite):
    # Classes always contain 2 parts:
    # 1. the __init__ section where you define all attributes
    # Init, only runs once. When the object is instantiated
    # Because this is a subclass, we need to call the parent's (Sprite) __init__

    def __init__(self, image, start_x,start_y):
        super(Player,self).__init__()
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image,(150,150))
        self.x = start_x
        self.y = start_y
        self.speed = 10
        self.screen = screen
    #2 The methods where you define all the class functions (methods)

    def draw_me(self):
        self.screen.blit(self.image, [self.x,self.y])

    def should_move(self,direction,yes_or_no):
        if(direction == "up"):
            # the up key is down. update self.
            self.should_move_up = yes_or_no
        if(direction == "down"):
            self.should_move_down = yes_or_no
        if(direction == "left"):
            self.should_move_left = yes_or_no
        if(direction == "right"):
            self.should_move_right = yes_or_no
