import pygame
import sys
import os
import xml.etree.ElementTree as ET
from arcade_machine import ArcadeMachine


def setup_machines(screen, machines):
    if os.path.isfile('romlist/exported.xml'):
        try:
            root = ET.parse('romlist/exported.xml').getroot()
            arcade_x = 100
            for machine in root.findall("./machine"):
                name = machine.get('name')
                description = machine.find("description").text
                new_machine = ArcadeMachine(screen)
                new_machine.name = name
                new_machine.set_game_image()
                new_machine.rect.centerx = arcade_x
                arcade_x += 100
                machines.add(new_machine)
        except ET.ParseError:
            print("Empty rom list.\nGet exported.xml from mame and place it in the rom list folder.")


def check_events(player, machines):
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
            elif event.key == pygame.K_g:
                start_active_machine(player, machines)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                player.moving_right = False
            if event.key == pygame.K_LEFT:
                player.moving_left = False
            if event.key == pygame.K_UP:
                player.moving_up = False
            if event.key == pygame.K_DOWN:
                player.moving_down = False


def check_player_collision(screen, player, machines):
    collisions = pygame.sprite.spritecollide(player, machines, dokill=False)
    if collisions:
        for machine in collisions:
            machine.activate()
            display_game_image(screen, machine)
    if not collisions:
        for machine in machines:
            machine.deactivate()


def display_game_image(screen, machine):
    if machine.get_title_image():
        game_image = machine.get_title_image()
        game_image_rect = game_image.get_rect()
        game_image_rect.centerx = screen.get_width() - screen.get_width()/6
        game_image_rect.centery = screen.get_height()/4
        screen.blit(game_image, game_image_rect)


def start_active_machine(player, machines):
    collisions = pygame.sprite.spritecollide(player, machines, dokill=False)
    if collisions:
        for machine in collisions:
            machine.start_game()
