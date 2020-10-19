import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, settings):
        super().__init__()
        self.speed = 5
        self.player_x = settings.screen_width / 2
        self.player_y = settings.screen_height / 2
        self.player_w = 20
        self.player_h = 40
        self.surface = pygame.Surface((self.player_w, self.player_h))
        self.surface.fill((250, 100, 10))
        self.rect = self.surface.get_rect(center=(self.player_x, self.player_y))
