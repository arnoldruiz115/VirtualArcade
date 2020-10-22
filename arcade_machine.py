import pygame
import subprocess
import os.path


class ArcadeMachine(pygame.sprite.Sprite):
    def __init__(self, screen):
        super(ArcadeMachine, self).__init__()
        self.screen = screen
        self.pos_x = 600
        self.pos_y = 400
        self.width = 50
        self.height = 80
        self.image_on = pygame.image.load('images/arcade_machine.png').convert_alpha()
        self.image_off = pygame.image.load('images/arcade_machine_off.png').convert_alpha()
        self.image = self.image_off
        self.active = False
        self.rect = self.image.get_rect()
        self.rect.centerx = float(self.pos_x)
        self.rect.bottom = float(self.pos_y)
        self.name = ""
        self.game_title_image = pygame.image.load('images/title/no_image.png').convert()

    def activate(self):
        if not self.active:
            self.active = True
            self.image = self.image_on

    def deactivate(self):
        if self.active:
            self.active = False
            self.image = self.image_off

    def set_game_image(self):
        if os.path.isfile('images/title/{}.png'.format(self.name)):
            self.game_title_image = pygame.image.load('images/title/{}.png'.format(self.name)).convert()

    def get_title_image(self):
        return self.game_title_image

    def start_game(self):
        if self.active:
            print("Starting {}".format(self.name))
            subprocess.Popen([r"C:\Users\Arnold\Desktop\mame\mame64.exe", self.name])
