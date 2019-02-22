import pygame
import random
from pygame.locals import *


class Player(pygame.sprite.Sprite):

    def __init__(self):

        super().__init__()
        # Create an image
        self.image = pygame.Surface([40, 60])
        self.image.fill((0, 0, 255))

        # Set a referance to the image rect.
        self.rect = self.image.get_rect()

        # Set speed vector of player
        self.change_x = 0
        self.change_y = 0


    def update(self):
        self.gravity()

        self.rect.x += self.change_x

        collisions = pygame.sprite.spritecollide(self, self.map.platforms, False)
        for collide in collisions:
            if self.change_x > 0:
                self.rect.right = collide.rect.left
            elif self.change_x < 0:
                self.rect.left = collide.rect.right

        self.rect.y += self.change_y

        collisions = pygame.sprite.spritecollide(self, self.map.platforms, False)
        for collide in collisions:
            if self.change_y < 0:
                self.rect.top = collide.rect.bottom
            elif self.change_y > 0:
                self.rect.bottom = collide.rect.top

            self.change_y = 0

    def gravity(self):

        # Calculate for gravity

        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .35

        # These numbers are the screens height should create global variables later

        if self.rect.y >= 600 - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = 600 - self.rect.height

    def up(self):
        # jumping

        # By moving down 2 pixels we check if we are under anything before trying to jump
        # NOTE negative is up. Positive is Down.
        self.rect.y += 2
        platforms_collisions = pygame.sprite.spritecollide(self, self.map.platforms, False)
        self.rect.y -= 2

        # Screen height used here again, also the len is checking to see if there is any platform
        # to be collided with in the list
        if len(platforms_collisions) > 0 or self.rect.bottom >= 600:
            self.change_y = -10

    def left(self):
        self.change_x = -6

    def right(self):
        self.change_x = 6

    def stop(self):
        self.change_x = 0


class Platform(pygame.sprite.Sprite):

    def __init__(self, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill((255, 255, 0))

        self.rect = self.image.get_rect()


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


def main():
    # I do need to neaten this up
    pygame.init()

    # Create Screen
    screen = [800, 600]
    screen = pygame.display.set_mode(screen)

    # Create player
    player = Player()

    # Create the map

    map_list = []
    # Append it to the map list, the map and the player cast inside it.
    map_list.append(Map_1(player))

    # Initialize the Sprite Group
    sprites = pygame.sprite.Group()

    # Put the player.map in a map
    player.map = map_list[0]

    # Create the size of the player
    player.rect.x = 340
    player.rect.y = 600 - player.rect.height
    sprites.add(player)

    # Not entirely sure about the clock stuff but it told me to put clock in

    clock = pygame.time.Clock()

    # Set the main loop parameter
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.left()
                if event.key == pygame.K_RIGHT:
                    player.right()
                if event.key == pygame.K_UP:
                    player.up()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player.change_x < 0:
                    player.stop()
                if event.key == pygame.K_RIGHT and player.change_x > 0:
                    player.stop()

        sprites.update()
        map_list[0].update()

        if player.rect.left >= 500:
            diff = player.rect.left - 500
            player.rect.left = 500
            map_list[0].scroll(-diff)

        # If the player gets near the left side, shift the world right (+x)
        if player.rect.right <= 120:
            diff = 120 - player.rect.right
            player.rect.right = 120
            map_list[0].scroll(diff)



        # All drawing code goes at the bottom of the main event loop
        map_list[0].draw(screen)
        sprites.draw(screen)

        clock.tick(60)
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
