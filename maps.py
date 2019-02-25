import pygame
from pygame import *
from platforms import Platform

# this is the class that allows each map to be made
class Map():

    def __init__(self, player):
        self.platforms = pygame.sprite.Group()
        self.player = player

        # how much scrolled left or right
        self.world_scroll = 0

    def update(self):
        self.platforms.update()

    def draw(self, screen):
        screen.fill((0, 255, 0))

        # Draw all the sprites
        self.platforms.draw(screen)

    def scroll(self, shift_x):
        self.world_scroll += shift_x

        # Move all the platforms in the list

        for platform in self.platforms:
            platform.rect.x += shift_x

# This is the class that actually creates each map, this is the method to make more
class Map_1(Map):
    # Create a new class for every map made

    def __init__(self, player):
        Map.__init__(self, player)

        # The length of the map make it negative to act as a positive
        self.map_limit = -3000

        # Create an array holding (width,height,x,y) I will randomly generate these later

        map = [[210, 20, 500, 450],
               [510, 70, 680, 490],
               [210, 70, 990, 360],
               [210, 70, 1230, 320],
               [210, 70, 1460, 190],
               [210, 70, 1790, 420]]

        for platform in map:
            # Pass the width and height to the Platform Class
            plat = Platform(platform[0], platform[1])
            plat.rect.x = platform[2]
            plat.rect.y = platform[3]
            # Put it in the player class so it can be applied to collisions
            plat.player = self.player
            # add it to the platforms list of collisions
            self.platforms.add(plat)