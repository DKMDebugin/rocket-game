import sys
import pygame

def check_events(rocket):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #if the quit event is triggered
            sys.exit() # exit game

        elif event.type == pygame.KEYDOWN: #When key is pressed
            check_keydown_events(event, rocket)

        elif event.type == pygame.KEYUP: #When key is released
            check_keyup_events(event, rocket)

def check_keydown_events(event, rocket):
    """Respond to keypresses."""
    if event.key == pygame.K_RIGHT:
        rocket.moving_right = True
    elif event.key == pygame.K_LEFT:
        rocket.moving_left = True
    elif event.key == pygame.K_UP:
        rocket.moving_up = True
    elif event.key == pygame.K_DOWN:
        rocket.moving_down = True

def check_keyup_events(event, rocket):
    """Respond to key releases."""
    if event.key == pygame.K_RIGHT:
        rocket.moving_right = False
    elif event.key == pygame.K_LEFT:
        rocket.moving_left = False
    elif event.key == pygame.K_UP:
        rocket.moving_up = False
    elif event.key == pygame.K_DOWN:
        rocket.moving_down = False

def update_screen(rg_settings, screen, rocket):
    """Update images on the screen and flip to the new screen."""

    screen.fill(rg_settings.bg_color) #Redraw the screen during each pass through the loop.
    rocket.blitme() #Redraw rocket at its current location
    pygame.display.flip() # Make the most recently drawn screen visible.
