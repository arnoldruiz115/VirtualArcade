import pygame
import sys
from settings import Settings
from player import Player


def run_game():
    pygame.init()
    settings = Settings()

    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    bg = (200, 170, 255)

    player = Player(settings)
    sprites = pygame.sprite.Group()
    sprites.add(player)

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(bg)
        for entity in sprites:
            screen.blit(entity.surface, entity.rect)
        pygame.display.update()


run_game()
