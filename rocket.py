import pygame

class Rocket():
    '''
    Rocket() helps manage most of the behaviour of the player's rocket
    '''
    def __init__(self, rg_settings, screen):
        """Initialize the rocket and set its starting position."""
        #initialize the parameters
        self.screen = screen
        self.rg_settings = rg_settings
        # Load the rocket image and get its rect.
        self.image = pygame.image.load('images/rocket.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # Start each new rocket at the center of the screen.
        self.rect.center = self.screen_rect.center #center attribute position game element at the center.

        #Store a decimal value for the rocket's center
        self.center = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        #Movement flag
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        '''
        Update the rocket's position based on the movement flag.
        '''
        #Update the ship's center value, not the rect.
        if  self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.rg_settings.rocket_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.rg_settings.rocket_speed_factor
        if  self.moving_up and self.rect.top > 0:
            self.centery -= self.rg_settings.rocket_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.rg_settings.rocket_speed_factor

        #Update rect object from self.center
        self.rect.centerx = self.center
        self.rect.centery = self.centery

    def blitme(self):
        """Draw the rocket at its current location."""
        self.screen.blit(self.image, self.rect)
