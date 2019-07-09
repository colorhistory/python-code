import pygame


class Ship:

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screenRect = ai_game.screen.get_rect()

        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screenRect.midbottom

    def blitme(self):
        self.screen.blit(self.image, self.rect)
