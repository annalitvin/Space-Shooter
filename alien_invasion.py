import sys

import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    pygame.init()
    ai_settings = Settings()
    #Создаем объект экрана
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    bg_color = (ai_settings.bg_color)
    ship = Ship(ai_settings, screen)

    # Создание группы для хранения пуль.
    bullets = Group()

    #Запуск основного цикла игры
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        gf.update_screen(ai_settings, screen, ship, bullets)
        screen.fill(ai_settings.bg_color)
        ship.blitme()

        #Отображение последнего  прорисованного экрана
        pygame.display.flip()
run_game()