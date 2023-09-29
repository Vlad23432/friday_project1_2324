import sys
import pygame as pg
from settings import Settings
def run_game():
    ai_settings = Settings()


    pg.init()  # инициализируем pygame
    screen = pg.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))  # создаем экран игры разрешением 1280х720px
    pg.display.set_caption('alien invasion')
    while True:  # цикл игры
        for event in pg.event.get():  # обработчик событий pygame
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
        screen.fill(ai_settings.bg_color)
        pg.display.flip()


run_game()