import pygame
import game_functions as gf
from settings import Settings
from player import Player
from arcade_machine import ArcadeMachine


def run_game():
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    bg = (200, 170, 255)

    player = Player(settings, screen)
    machines = pygame.sprite.Group()

    street_fighter_arcade = ArcadeMachine(screen)
    street_fighter_arcade.name = "Street Fighter"
    tetris_arcade = ArcadeMachine(screen)
    tetris_arcade.name = "Tetris"
    tetris_arcade.rect.centerx = 900
    machines.add(street_fighter_arcade)
    machines.add(tetris_arcade)

    run = True
    while run:
        screen.fill(bg)
        machines.draw(screen)
        gf.check_events(player, machines)
        player.draw()
        player.update()
        gf.check_player_collision(player, machines)
        pygame.display.update()


run_game()
