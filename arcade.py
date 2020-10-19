import pygame
import game_functions as gf
from settings import Settings
from player import Player


def run_game():
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    bg = (200, 170, 255)

    player = Player(settings, screen)

    run = True
    while run:
        screen.fill(bg)
        gf.check_events(player)
        player.blitme()
        player.update()
        pygame.display.update()


run_game()
