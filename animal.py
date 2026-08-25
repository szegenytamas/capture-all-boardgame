import pygame
from constants import CELL_SIZE


class Animal:
    def __init__(self, _score=None, _pos=None, _color=None, _image_path=None):
        self.color = _color
        self.pos = _pos
        self.score = _score
        self.is_caught = False
        self.image = pygame.image.load(_image_path).convert_alpha()
        self.who_caught_me = None

        cx = self.pos.x*CELL_SIZE + CELL_SIZE/2
        cy = self.pos.y*CELL_SIZE + CELL_SIZE/2
        self.animal_rect = self.image.get_rect(center=(cx, cy))
        self.rect = pygame.Rect(
            self.pos.x*CELL_SIZE, self.pos.y*CELL_SIZE, CELL_SIZE, CELL_SIZE)

    def draw_animal(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        screen.blit(self.image, self.animal_rect)
        if self.is_caught:
            pygame.draw.line(
                screen, self.who_caught_me, self.rect.topleft, self.rect.bottomright, 3)
            pygame.draw.line(
                screen, self.who_caught_me, self.rect.topright, self.rect.bottomleft, 3)
        pygame.draw.rect(screen, 'black', self.rect, 1)
