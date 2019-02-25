import pygame
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
