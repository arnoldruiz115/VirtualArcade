import pygame
import sys

def check_events(player):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player.moving_right = True
                player.moving_left = False
            elif event.key == pygame.K_LEFT:
                player.moving_right = False
                player.moving_left = True
            elif event.key == pygame.K_UP:
                player.moving_down = False
                player.moving_up = True
            elif event.key == pygame.K_DOWN:
                player.moving_up = False
                player.moving_down = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                player.moving_right = False
            if event.key == pygame.K_LEFT:
                player.moving_left = False
            if event.key == pygame.K_UP:
                player.moving_up = False
            if event.key == pygame.K_DOWN:
                player.moving_down = False