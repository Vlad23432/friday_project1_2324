import pygame as pg
import game_fuctions as gf
from settings import Settings
from ship import Ship
from pygame.sprite import Group


def run_game():
    ai_settings = Settings()

    pg.init()  # инициализируем pygame
    screen = pg.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))  # создаем экран игры разрешением 1280х720px
    pg.display.set_caption("Alien Invasion")  # название окна игры

    ship = Ship(ai_settings, screen)
    aliens = Group()
    bullets = Group()

    while True:  # цикл игры
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, bullets, aliens)
        gf.create_fleet(ai_settings, screen, aliens, ship)

run_game()  # вызываем игровую функцию