import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, settings, screen):
        super().__init__()
        self.screen = screen
        self.speed = 5
        self.player_x = settings.screen_width / 2
        self.player_y = settings.screen_height / 2
        self.player_w = 20
        self.player_h = 40
        self.surface = pygame.Surface((self.player_w, self.player_h))
        self.surface.fill((250, 100, 10))
        self.center = (self.player_x, self.player_y)
        self.rect = self.surface.get_rect()
        self.rect.centerx = float(self.player_x)
        self.rect.bottom = float(self.player_y)

        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False

    def blitme(self):
        self.screen.blit(self.surface, self.rect)

    def update(self):
        if self.moving_left:
            self.rect.centerx -= 1
        if self.moving_right:
            self.rect.centerx += 1
        if self.moving_up:
            self.rect.bottom -= 1
        if self.moving_down:
            self.rect.bottom += 1

