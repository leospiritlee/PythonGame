import pygame

from setting import Settings
from ship import Ship
import game_function as gf

def run_game():

    pygame.init()

    al_setting = Settings()

    screen = pygame.display.set_mode((al_setting.screen_width,al_setting.screen_height))
    pygame.display.set_caption('Alien Invasion')

    ship = Ship(al_setting,screen)

    while True:

        gf.check_events(ship)
        ship.update()
        gf.update_screen(al_setting,screen,ship)


run_game()

