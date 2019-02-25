import pygame
import random
from pygame.locals import *
from player import Player
from platforms import Platform
from maps import *

def main():
    # Settings Function (init_game) - Start
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
    
    # Settings Function (init_game) - Stop
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
