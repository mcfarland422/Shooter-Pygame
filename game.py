# Duh
# We have access to pygame, because we did:
#$ pip install pygame
#it is NOT part of core. This is a 3rd party module.
import pygame

from Player import Player

# Have to init the pygame object so we can use it

pygame.init()

# Screen size is a tuple
screen_size = (1000,800)
# Because we are going to paint the background, we need a tuple for color
background_color = (82,111,53)

# Create a screen for pygame to use to draw on
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("An epic shooter made with pygame")

the_player = Player('heroMM.png',100,100,screen)

# the_player_image = pygame.image.load('heroMM.png')
# player = {
#     "x": 100,
#     "y": 100
# }

game_on = True
# Set up the main game loop
while game_on: #will run forever (until break)
    # Loop through all the pygame events.
    # This is pygames escape hatch. (Quit)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_on = False
        elif event.type == pygame.KEYDOWN:
            #print "User pressed a key!!"
            if event.key == 273:
                # user pressed up
                the_player.should_move("up",True)
            elif event.key == 274:
                the_player.should_move("down",True)
            elif event.key == 275:
                the_player.should_move("right",True)
            elif event.key == 276:
                the_player.should_move("left",True)


    #paint the screen
    screen.fill(background_color)

    #Must be after fill, or we won't be able to see the hero
    screen.blit(the_player_image, [play["x"],player["y"]])

    #flip the screen, i.e.clear it so we can draw again... and again... and again
    pygame.display.flip()
