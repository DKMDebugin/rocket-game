import pygame

from settings import Settings
from rocket import Rocket
import game_function as gf

def run_game():
    '''
    Initialize pygame ,
    create settings instance &
    a screen object (window screen size & window caption) 
    '''
    pygame.init()
    rg_settings = Settings() #Object of Settings() class
    screen = pygame.display.set_mode(
    (rg_settings.screen_width, rg_settings.screen_height)) #set screen size by passing in Settings width & height attributes
    pygame.display.set_caption("Rocket Game")

    #Make a ship
    rocket = Rocket(rg_settings, screen)

    # Start the main loop for the game.
    while True:
        gf.check_events(rocket)# Watch for keyboard and mouse events.
        rocket.update() #Updates the ship postion
        #Update images on the screen and flip to the new screen.
        gf.update_screen(rg_settings, screen, rocket)




run_game()
