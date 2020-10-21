import pygame


class ArcadeMachine(pygame.sprite.Sprite):
    def __init__(self, screen):
        super(ArcadeMachine, self).__init__()
        self.screen = screen
        self.pos_x = 600
        self.pos_y = 400
        self.width = 50
        self.height = 80
        self.image = pygame.image.load('images/arcade_machine_off.png')
        self.active = False
        self.rect = self.image.get_rect()
        self.rect.centerx = float(self.pos_x)
        self.rect.bottom = float(self.pos_y)
        self.name = ""

    def activate(self):
        if not self.active:
            self.active = True
            self.image = pygame.image.load('images/arcade_machine.png')

    def deactivate(self):
        if self.active:
            self.active = False
            self.image = pygame.image.load('images/arcade_machine_off.png')

    def start_game(self):
        if self.active:
            print("Starting {}".format(self.name))
