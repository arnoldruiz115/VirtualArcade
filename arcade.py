import pygame
import game_functions as gf
from settings import Settings
from player import Player


def run_game():
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    bg = (200, 170, 255)
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 30)

    player = Player(settings, screen)
    machines = pygame.sprite.Group()
    gf.setup_machines(screen, machines)

    run = True
    while run:
        screen.fill(bg)
        machines.draw(screen)
        gf.check_events(player, machines)
        player.draw()
        player.update()
        fps = font.render(str(int(clock.get_fps())), True, pygame.Color('white'))
        screen.blit(fps, (50, 50))
        gf.check_player_collision(screen, player, machines)
        pygame.display.update()
        clock.tick(120)


run_game()
